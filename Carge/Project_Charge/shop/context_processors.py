from django.conf import settings

from .cart import get_cart


def cart_summary(request):
    cart = get_cart(request)
    try:
        count = sum(cart.values())
    except TypeError:
        count = 0
    return {"cart_count": count}


def account_pricing(request):
    pct = getattr(settings, "REGISTERED_USER_DISCOUNT_PERCENT", 0) or 0
    return {
        "registered_discount_percent": pct,
        "user_has_registered_discount": bool(
            getattr(request, "user", None) and request.user.is_authenticated
        ),
    }
