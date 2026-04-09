"""Підбір статичного прев’ю для категорії (ім’я + slug) — відповідає типу товару Charge."""


def stock_slug_for_category(name: str, slug: str) -> str:
    n = (name or "").lower()
    s = (slug or "").lower()

    if "віртуаль" in n or "vr" in s or "virtual" in s:
        return "vr"
    if ("окуляр" in n or "очк" in n) and "віртуаль" not in n:
        return "glasses"
    if "ноутбук" in n or "notebook" in s or "laptop" in s:
        return "laptop"
    if "планшет" in n or "tablet" in s:
        return "tablet"
    if "смартфон" in n or "smartphone" in s:
        return "smartphone"
    if "телефон" in n or "phone" in s:
        return "phone"
    if "навушник" in n or "headphone" in s or "headset" in s:
        return "headphones"
    if "годинник" in n or "watch" in s:
        return "watch"
    if "монітор" in n or "monitor" in s:
        return "monitor"
    if "клавіатур" in n or "keyboard" in s:
        return "keyboard"
    if "миш" in n or "mouse" in s:
        return "mouse"
    if "колонк" in n or "speaker" in s or "bluetooth" in n or "блютуз" in n:
        return "speaker"
    if "повербанк" in n or "powerbank" in s or "power-bank" in s:
        return "powerbank"
    if "роутер" in n or "router" in s or "wi-fi" in n or "wifi" in s:
        return "router"
    if "комп" in n or "пк" in n or "pc" in s or "computer" in s or "desktop" in s:
        return "computer"
    return "gadget"


def stock_url_for_category(name: str, slug: str) -> str:
    from django.templatetags.static import static

    slug_key = stock_slug_for_category(name, slug)
    return static(f"shop/showcase/{slug_key}.jpg")
