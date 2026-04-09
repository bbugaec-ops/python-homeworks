# Generated manually for Charge — групи марок у каталозі

from django.db import migrations, models


def backfill_brand_from_title(apps, schema_editor):
    Product = apps.get_model("shop", "Product")
    for p in Product.objects.iterator():
        title = (p.title or "").strip()
        brand = (p.brand or "").strip()
        if not brand and title:
            first = title.split(None, 1)[0]
            Product.objects.filter(pk=p.pk).update(brand=first)


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0002_verbose_slug_labels"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="brand",
            field=models.CharField(
                blank=True,
                help_text="Для груп на сторінці каталогу. Якщо порожньо — візьметься перше слово з назви.",
                max_length=100,
                verbose_name="Марка",
            ),
        ),
        migrations.AlterModelOptions(
            name="product",
            options={
                "ordering": ["category", "brand", "title"],
                "verbose_name": "Товар",
                "verbose_name_plural": "Товари",
            },
        ),
        migrations.RunPython(backfill_brand_from_title, migrations.RunPython.noop),
    ]
