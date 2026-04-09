CART_SESSION_KEY = "charge_cart"


def get_cart(request):
    raw = request.session.get(CART_SESSION_KEY)
    if not isinstance(raw, dict):
        return {}
    out = {}
    for k, v in raw.items():
        try:
            out[str(k)] = int(v)
        except (TypeError, ValueError):
            continue
    return out


def set_cart(request, cart):
    request.session[CART_SESSION_KEY] = cart
    request.session.modified = True
