from decimal import Decimal

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.decorators.http import require_POST

from .cart import get_cart, set_cart
from .models import Product


def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', {'products': products})


def _lines_and_total(request):
    cart = get_cart(request)
    lines = []
    total = Decimal('0')
    pruned = {}
    for pid, qty in cart.items():
        try:
            p = Product.objects.get(pk=int(pid))
        except (ValueError, Product.DoesNotExist):
            continue
        pruned[pid] = qty
        sub = p.price * qty
        total += sub
        lines.append({'product': p, 'qty': qty, 'subtotal': sub})
    if pruned != cart:
        set_cart(request, pruned)
    return lines, total


def cart_view(request):
    lines, total = _lines_and_total(request)
    return render(request, 'shop/cart.html', {'lines': lines, 'total': total})


@require_POST
def cart_add(request, slug):
    product = get_object_or_404(Product, slug=slug)
    cart = get_cart(request)
    key = str(product.pk)
    cart[key] = cart.get(key, 0) + 1
    set_cart(request, cart)
    next_url = request.POST.get('next') or reverse('shop:product_list')
    return redirect(next_url)


@require_POST
def cart_remove(request, slug):
    product = get_object_or_404(Product, slug=slug)
    cart = get_cart(request)
    key = str(product.pk)
    cart.pop(key, None)
    set_cart(request, cart)
    return redirect(reverse('shop:cart'))


@require_POST
def cart_update(request):
    cart = get_cart(request)
    for key in list(cart.keys()):
        field = f'qty_{key}'
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
    return redirect(reverse('shop:cart'))
