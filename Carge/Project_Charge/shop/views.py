from decimal import Decimal, InvalidOperation

from django.contrib import messages
from django.contrib.auth import login
from django.conf import settings
from django.db.models import Max, Min
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.decorators.http import require_POST

from .cart import get_cart, set_cart
from .forms import ChargeUserCreationForm
from .models import Category, Product, Order, OrderItem, OrderCreateForm
from .pricing import unit_price_for_user
from .showcase_assets import stock_slug_for_category, stock_url_for_category


def order_create(request):
    lines, total = _cart_lines_and_total(request)

    if not lines:
        return redirect('product_list')

    if request.method == "POST":
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()

            for item in lines:
                unit = unit_price_for_user(item["product"], request.user)
                OrderItem.objects.create(
                    order=order,
                    product=item["product"],
                    price=unit,
                    quantity=item["qty"],
                )

            set_cart(request, {})

            return render(request, "shop/order_success.html", {"order": order})
    else:
        form = OrderCreateForm()

    return render(
        request,
        "shop/order_create.html",
        {
            "form": form,
            "lines": lines,
            "total": total,
        },
    )


def signup(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        form = ChargeUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            pct = getattr(settings, "REGISTERED_USER_DISCOUNT_PERCENT", 3)
            messages.success(
                request,
                f"Реєстрація пройшла успішно. Знижка {pct}% діє на ціни в кошику та при оформленні замовлення.",
            )
            return redirect("home")
    else:
        form = ChargeUserCreationForm()
    return render(request, "shop/signup.html", {"form": form})


def _cart_lines_and_total(request):
    cart = get_cart(request)
    lines = []
    total = Decimal("0")
    pruned = {}
    pks = []
    for pid, qty in cart.items():
        try:
            pks.append(int(pid))
        except ValueError:
            continue
    by_pk = {
        p.pk: p
        for p in Product.objects.select_related("category").filter(pk__in=pks)
    }
    for pid, qty in cart.items():
        try:
            pk = int(pid)
        except ValueError:
            continue
        p = by_pk.get(pk)
        if p is None:
            continue
        if qty <= 0:
            continue
        pruned[pid] = qty
        unit = unit_price_for_user(p, request.user)
        sub = unit * qty
        total += sub
        lines.append(
            {
                "product": p,
                "qty": qty,
                "subtotal": sub,
                "unit_price": unit,
            }
        )
    if pruned != cart:
        set_cart(request, pruned)
    return lines, total


def cart_view(request):
    lines, total = _cart_lines_and_total(request)
    for line in lines:
        p = line["product"]
        if p.category_id:
            p.showcase_fallback_url = stock_url_for_category(
                p.category.name, p.category.slug or ""
            )
        else:
            p.showcase_fallback_url = stock_url_for_category("", "")
    return render(
        request,
        "shop/cart.html",
        {"lines": lines, "total": total},
    )


@require_POST
def cart_add(request, slug):
    product = get_object_or_404(Product, slug=slug)
    cart = get_cart(request)
    key = str(product.pk)
    cart[key] = cart.get(key, 0) + 1
    set_cart(request, cart)
    next_url = request.POST.get("next") or reverse("product_list")
    return redirect(next_url)


@require_POST
def cart_increment(request, pk):
    product = get_object_or_404(Product, pk=pk)
    cart = get_cart(request)
    key = str(product.pk)
    cart[key] = cart.get(key, 0) + 1
    set_cart(request, cart)
    return redirect(reverse("cart"))


@require_POST
def cart_decrement(request, pk):
    product = get_object_or_404(Product, pk=pk)
    cart = get_cart(request)
    key = str(product.pk)
    q = cart.get(key, 0)
    if q <= 1:
        cart.pop(key, None)
    else:
        cart[key] = q - 1
    set_cart(request, cart)
    return redirect(reverse("cart"))


@require_POST
def cart_remove(request, pk):
    product = get_object_or_404(Product, pk=pk)
    cart = get_cart(request)
    cart.pop(str(product.pk), None)
    set_cart(request, cart)
    return redirect(reverse("cart"))


@require_POST
def cart_update(request):
    cart = get_cart(request)
    for key in list(cart.keys()):
        field = f"qty_{key}"
        if field not in request.POST:
            continue
        try:
            q = int(request.POST[field])
        except ValueError:
            continue
        if q <= 0:
            cart.pop(key, None)
        else:
            cart[key] = q
    set_cart(request, cart)
    return redirect(reverse("cart"))


def _category_by_predicate(categories, used_ids, pred):
    for c in categories:
        if c.pk in used_ids:
            continue
        n = (c.name or "").lower()
        s = (c.slug or "").lower()
        if pred(n, s):
            used_ids.add(c.pk)
            return c
    return None


def home(request):
    """Головна — тайли категорій (окуляри без тайла на головній)."""
    categories = list(Category.objects.all().order_by("name"))

    # (fallback якщо категорії немає, предикат, опційно підпис для тайла)
    pinned = [
        (
            "Смартфони",
            lambda n, s: "телефон" in n or "смартфон" in n or "phone" in s,
            "Смартфони",
        ),
        ("Ноутбук", lambda n, s: "ноутбук" in n),
        ("Планшет", lambda n, s: "планшет" in n),
        (
            "Віртуальна реальність",
            lambda n, s: "віртуаль" in n or "vr" in s or "virtual" in s,
        ),
    ]

    used = set()
    covered_slugs = set()
    showcase = []
    for entry in pinned:
        if len(entry) == 3:
            fallback_label, pred, label_override = entry
        else:
            fallback_label, pred = entry
            label_override = None
        c = _category_by_predicate(categories, used, pred)
        name = c.name if c else fallback_label
        slug = c.slug if c else ""
        if label_override == "Смартфони":
            illus_name, illus_slug = "Смартфони", ""
        else:
            illus_name, illus_slug = name, slug
        illustration = stock_url_for_category(illus_name, illus_slug)
        covered_slugs.add(stock_slug_for_category(illus_name, illus_slug))
        display_label = (
            label_override if label_override is not None else (c.name if c else fallback_label)
        )
        showcase.append(
            {
                "label": display_label,
                "category_id": c.pk if c else None,
                "image_url": illustration,
            }
        )

    for c in categories:
        if c.pk in used:
            continue
        sk = stock_slug_for_category(c.name, c.slug or "")
        if sk == "glasses":
            continue
        if sk in covered_slugs:
            continue
        covered_slugs.add(sk)
        illustration = stock_url_for_category(c.name, c.slug or "")
        showcase.append(
            {
                "label": c.name,
                "category_id": c.pk,
                "image_url": illustration,
            }
        )

    return render(request, "shop/home.html", {"showcase": showcase})


def product_list(request, category_id=None):
    qs = Product.objects.select_related("category")
    category = None
    if category_id is not None:
        category = get_object_or_404(Category, pk=category_id)
        qs = qs.filter(category=category)

    raw_min = (request.GET.get("price_min") or "").strip()
    raw_max = (request.GET.get("price_max") or "").strip()
    price_errors = []
    parsed_min = parsed_max = None

    if raw_min:
        try:
            d = Decimal(raw_min.replace(",", "."))
            if d < 0:
                price_errors.append("«Від»: ціна не може бути від'ємною.")
            else:
                parsed_min = d
        except InvalidOperation:
            price_errors.append("«Від»: введіть число (наприклад 500 або 1299.99).")

    if raw_max:
        try:
            d = Decimal(raw_max.replace(",", "."))
            if d < 0:
                price_errors.append("«До»: ціна не може бути від'ємною.")
            else:
                parsed_max = d
        except InvalidOperation:
            price_errors.append("«До»: введіть число.")

    if (
        parsed_min is not None
        and parsed_max is not None
        and parsed_min > parsed_max
    ):
        price_errors.append("«Від» має бути менше або дорівнювати «До».")

    bounds = qs.aggregate(lo=Min("price"), hi=Max("price"))

    if not price_errors:
        if parsed_min is not None:
            qs = qs.filter(price__gte=parsed_min)
        if parsed_max is not None:
            qs = qs.filter(price__lte=parsed_max)

    products = list(qs)
    for p in products:
        if p.category_id:
            p.showcase_fallback_url = stock_url_for_category(
                p.category.name, p.category.slug or ""
            )
        else:
            p.showcase_fallback_url = stock_url_for_category("", "")
        p.unit_price = unit_price_for_user(p, request.user)

    filter_applied = not price_errors and (parsed_min is not None or parsed_max is not None)
    empty_filtered = filter_applied and not products

    return render(
        request,
        "shop/product_list.html",
        {
            "products": products,
            "current_category": category,
            "price_min_raw": raw_min,
            "price_max_raw": raw_max,
            "price_errors": price_errors,
            "price_bounds_lo": bounds["lo"],
            "price_bounds_hi": bounds["hi"],
            "filter_applied": filter_applied,
            "empty_filtered": empty_filtered,
        },
    )


def product_detail(request, slug):
    product = get_object_or_404(
        Product.objects.select_related("category"),
        slug=slug,
    )
    if product.category_id:
        showcase_fallback_url = stock_url_for_category(
            product.category.name, product.category.slug or ""
        )
    else:
        showcase_fallback_url = stock_url_for_category("", "")
    return render(
        request,
        "shop/product_detail.html",
        {
            "product": product,
            "showcase_fallback_url": showcase_fallback_url,
            "unit_price": unit_price_for_user(product, request.user),
        },
    )