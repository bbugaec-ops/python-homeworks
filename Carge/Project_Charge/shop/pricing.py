"""Ціни з урахуванням знижки для зареєстрованих користувачів."""

from decimal import ROUND_HALF_UP, Decimal

from django.conf import settings


def registered_discount_fraction() -> Decimal:
    pct = getattr(settings, "REGISTERED_USER_DISCOUNT_PERCENT", 0) or 0
    return Decimal(str(pct)) / Decimal("100")


def unit_price_for_user(product, user) -> Decimal:
    """Базова ціна товару з урахуванням знижки акаунта (якщо увійшов)."""
    base = product.price
    if not getattr(user, "is_authenticated", False):
        return base
    frac = registered_discount_fraction()
    if frac <= 0:
        return base
    out = base * (Decimal("1") - frac)
    return out.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
