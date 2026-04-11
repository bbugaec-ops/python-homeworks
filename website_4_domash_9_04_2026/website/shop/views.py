from decimal import Decimal, InvalidOperation

from django.shortcuts import get_object_or_404, render

from .models import Category, Product


def _parse_price(raw):
    if raw is None:
        return None
    s = str(raw).strip().replace(",", ".")
    if s == "":
        return None
    try:
        return Decimal(s)
    except (InvalidOperation, ValueError):
        return None


def _apply_filters_and_sort(queryset, request):
    """Фільтр і сортування з GET (спільно для каталогу і категорії)."""
    qs = queryset

    min_p = _parse_price(request.GET.get("min_price"))
    max_p = _parse_price(request.GET.get("max_price"))

    if min_p is not None:
        qs = qs.filter(price__gte=min_p)
    if max_p is not None:
        qs = qs.filter(price__lte=max_p)

    sort = (request.GET.get("sort") or "").strip()
    if sort == "price_asc":
        qs = qs.order_by("price", "id")
    elif sort == "price_desc":
        qs = qs.order_by("-price", "id")
    elif sort == "newest":
        qs = qs.order_by("-created_at", "id")
    else:
        qs = qs.order_by("id")

    return qs


def product_list(request):
    products = _apply_filters_and_sort(Product.objects.all(), request)
    categories = Category.objects.all()
    return render(
        request,
        "shop/product_list.html",
        {"products": products, "categories": categories},
    )


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, "shop/product_detail.html", {"product": product})


def category_products(request, slug):
    c = get_object_or_404(Category, slug=slug)
    base = Product.objects.filter(category=c)
    products = _apply_filters_and_sort(base, request)
    categories = Category.objects.all()
    return render(
        request,
        "shop/product_list.html",
        {
            "products": products,
            "categories": categories,
            "current_category": c,
        },
    )
