from .cart import get_cart


def cart_summary(request):
    cart = get_cart(request)
    try:
        count = sum(cart.values())
    except TypeError:
        count = 0
    return {'shop_cart_count': count}
