"""Генерує JPG-прев’ю категорій у стилі Charge (темний фон + золото). Запуск: python manage.py build_showcase

smartphone.jpg — «плитка» смартфона (400×400). phone.jpg — кнопковий телефон (240×320).
"""

from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand
from PIL import Image, ImageDraw


GOLD = "#ffc107"
BG = "#0c1222"
FILL = "#1a2744"
LINE = "#3d5a80"


def _save(out_dir: Path, name: str, draw_fn, size=(400, 400)):
    w, h = size
    img = Image.new("RGB", (w, h), BG)
    d = ImageDraw.Draw(img)
    draw_fn(d, w, h)
    path = out_dir / f"{name}.jpg"
    img.save(path, quality=90, optimize=True)


class Command(BaseCommand):
    help = "Створює shop/static/shop/showcase/*.jpg для головної сторінки"

    def handle(self, *args, **options):
        base = Path(settings.BASE_DIR) / "shop" / "static" / "shop" / "showcase"
        base.mkdir(parents=True, exist_ok=True)

        def smartphone(d, w, h):
            """Смартфон — великий екран (як було раніше для тайла «Смартфони»)."""
            d.rounded_rectangle([110, 48, 290, 352], radius=28, outline=GOLD, width=5)
            d.rounded_rectangle([125, 78, 275, 300], fill=FILL, outline=LINE, width=2)
            d.rounded_rectangle([138, 95, 262, 265], fill="#0d1f3c", outline=GOLD, width=1)
            d.rounded_rectangle([175, 310, 225, 325], fill=GOLD)

        def phone(d, w, h):
            """Кнопковий брусок (як старі Nokia / «для батьків»): канва 240×320."""
            cx = w // 2
            bw, bh = 74, 268
            x0, y0 = cx - bw // 2, 28
            x1, y1 = x0 + bw, y0 + bh
            d.rounded_rectangle([x0, y0, x1, y1], radius=14, outline=GOLD, width=3)
            pad = 9
            sx0, sy0 = x0 + pad, y0 + 11
            sx1, sy1 = x1 - pad, sy0 + 50
            d.rounded_rectangle([sx0, sy0, sx1, sy1], fill=FILL, outline=GOLD, width=2)
            for i in range(3):
                d.rectangle(
                    [sx0 + 6 + i * 8, sy0 + 6, sx0 + 10 + i * 8, sy0 + 9], fill=LINE
                )
            d.rectangle([sx1 - 18, sy0 + 6, sx1 - 6, sy0 + 9], fill=GOLD)
            d.line([(cx, sy0 + 16), (cx, sy1 - 8)], fill=LINE, width=1)
            d.line(
                [(sx0 + 10, (sy0 + sy1) // 2), (sx1 - 10, (sy0 + sy1) // 2)],
                fill=LINE,
                width=1,
            )
            sk_top = sy1 + 5
            sk_h = 9
            d.rounded_rectangle([sx0, sk_top, sx0 + 30, sk_top + sk_h], outline=LINE, width=1)
            d.rounded_rectangle([sx1 - 30, sk_top, sx1, sk_top + sk_h], outline=LINE, width=1)
            kw, kh, gx, gy = 17, 13, 3, 3
            kx0 = x0 + 11
            ky0 = sk_top + sk_h + 8
            for row in range(4):
                for col in range(3):
                    kx = kx0 + col * (kw + gx)
                    ky = ky0 + row * (kh + gy)
                    d.rounded_rectangle([kx, ky, kx + kw, ky + kh], radius=3, outline=GOLD, width=1)
            ny = y1 - 32
            d.ellipse([cx - 26, ny - 14, cx + 26, ny + 14], outline=GOLD, width=2)
            d.ellipse([cx - 7, ny - 5, cx + 7, ny + 5], fill=GOLD)

        def laptop(d, w, h):
            d.rounded_rectangle([60, 90, 340, 240], radius=6, outline=GOLD, width=4)
            d.rounded_rectangle([75, 105, 325, 220], fill=FILL, outline=LINE, width=1)
            d.polygon([(40, 255), (360, 255), (340, 285), (60, 285)], outline=GOLD, fill=FILL, width=3)

        def tablet(d, w, h):
            d.rounded_rectangle([100, 60, 300, 320], radius=20, outline=GOLD, width=5)
            d.rounded_rectangle([115, 80, 285, 290], fill=FILL, outline=LINE, width=2)
            d.ellipse([185, 300, 215, 315], fill=GOLD)

        def glasses(d, w, h):
            d.rounded_rectangle([70, 170, 170, 220], radius=30, outline=GOLD, width=4)
            d.rounded_rectangle([230, 170, 330, 220], radius=30, outline=GOLD, width=4)
            d.line([(170, 195), (230, 195)], fill=GOLD, width=4)

        def vr(d, w, h):
            d.arc([80, 140, 320, 280], start=180, end=360, fill=GOLD, width=5)
            d.rounded_rectangle([100, 165, 175, 235], radius=12, outline=GOLD, width=3)
            d.rounded_rectangle([225, 165, 300, 235], radius=12, outline=GOLD, width=3)
            d.line([(200, 120), (200, 160)], fill=GOLD, width=3)

        def headphones(d, w, h):
            d.arc([120, 100, 280, 220], start=180, end=360, fill=GOLD, width=6)
            d.rounded_rectangle([95, 175, 145, 270], radius=20, outline=GOLD, width=4)
            d.rounded_rectangle([255, 175, 305, 270], radius=20, outline=GOLD, width=4)

        def watch(d, w, h):
            d.rounded_rectangle([175, 110, 225, 260], radius=8, outline=GOLD, width=4)
            d.ellipse([155, 130, 245, 220], outline=GOLD, width=4)
            d.line([(200, 165), (200, 185)], fill=GOLD, width=3)
            d.line([(200, 185), (215, 195)], fill=GOLD, width=2)

        def monitor(d, w, h):
            d.rounded_rectangle([80, 70, 320, 230], radius=8, outline=GOLD, width=4)
            d.rounded_rectangle([95, 85, 305, 210], fill=FILL, outline=LINE, width=1)
            d.rectangle([185, 230, 215, 270], fill=GOLD, width=0)
            d.line([(150, 270), (250, 270)], fill=GOLD, width=4)

        def keyboard(d, w, h):
            d.rounded_rectangle([50, 160, 350, 240], radius=8, outline=GOLD, width=4)
            for i in range(8):
                x = 65 + i * 34
                d.rounded_rectangle([x, 175, x + 28, 195], outline=LINE, width=1)
            d.rounded_rectangle([120, 205, 280, 225], outline=LINE, width=1)

        def mouse(d, w, h):
            d.ellipse([150, 130, 250, 270], outline=GOLD, width=5)
            d.line([(200, 130), (200, 180)], fill=GOLD, width=2)

        def speaker(d, w, h):
            d.rounded_rectangle([140, 80, 260, 300], radius=16, outline=GOLD, width=4)
            d.ellipse([165, 120, 235, 190], outline=GOLD, width=3)
            d.ellipse([175, 210, 225, 260], outline=GOLD, width=2)

        def powerbank(d, w, h):
            d.rounded_rectangle([150, 100, 250, 280], radius=12, outline=GOLD, width=4)
            d.rectangle([175, 90, 225, 105], fill=GOLD)
            d.rounded_rectangle([170, 180, 230, 200], outline=LINE, width=2)

        def router(d, w, h):
            d.rounded_rectangle([80, 200, 320, 260], radius=6, outline=GOLD, width=4)
            d.line([(120, 200), (110, 140)], fill=GOLD, width=3)
            d.line([(200, 200), (200, 130)], fill=GOLD, width=3)
            d.line([(280, 200), (290, 150)], fill=GOLD, width=3)

        def computer(d, w, h):
            d.rounded_rectangle([220, 100, 310, 260], radius=4, outline=GOLD, width=3)
            d.rounded_rectangle([90, 70, 200, 180], radius=4, outline=GOLD, width=3)
            d.rounded_rectangle([100, 85, 190, 165], fill=FILL, width=0)
            d.polygon([(130, 190), (160, 190), (170, 220), (120, 220)], outline=GOLD, width=2)

        def gadget(d, w, h):
            d.rounded_rectangle([120, 120, 280, 260], radius=12, outline=GOLD, width=4)
            d.line([(140, 150), (260, 150)], fill=LINE, width=2)
            d.line([(140, 175), (240, 175)], fill=LINE, width=2)
            d.ellipse([175, 210, 225, 235], outline=GOLD, width=2)

        builders = {
            "smartphone": smartphone,
            "phone": phone,
            "laptop": laptop,
            "tablet": tablet,
            "glasses": glasses,
            "vr": vr,
            "headphones": headphones,
            "watch": watch,
            "monitor": monitor,
            "keyboard": keyboard,
            "mouse": mouse,
            "speaker": speaker,
            "powerbank": powerbank,
            "router": router,
            "computer": computer,
            "gadget": gadget,
        }

        sizes = {"phone": (240, 320)}
        for name, fn in builders.items():
            _save(base, name, fn, size=sizes.get(name, (400, 400)))
            self.stdout.write(f"OK {name}.jpg")

        self.stdout.write(self.style.SUCCESS(f"Готово: {base}"))
