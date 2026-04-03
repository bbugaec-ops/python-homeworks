CART_SESSION_KEY = 'shop_cart'


def get_cart(request):
    raw = request.session.get(CART_SESSION_KEY, {})
    if not isinstance(raw, dict):
        return {}
    out = {}
    for k, v in raw.items():
        try:
            q = int(v)
            if q > 0:
                out[str(k)] = q
        except (TypeError, ValueError):
            continue
    return out


def set_cart(request, cart):
    request.session[CART_SESSION_KEY] = cart
    request.session.modified = True
