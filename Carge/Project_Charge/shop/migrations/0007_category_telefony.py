# Категорія «Телефони» для кнопкових/мобільних телефонів (якщо ще немає).

from django.db import migrations


def forwards(apps, schema_editor):
    Category = apps.get_model("shop", "Category")
    if Category.objects.filter(name__iexact="Телефони").exists():
        return
    if Category.objects.filter(slug="telefony").exists():
        return
    Category.objects.create(name="Телефони", slug="telefony")


def backwards(apps, schema_editor):
    Category = apps.get_model("shop", "Category")
    Category.objects.filter(slug="telefony").delete()


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0006_order_orderitem"),
    ]

    operations = [
        migrations.RunPython(forwards, backwards),
    ]
