# Повернення каталогу до попереднього вигляду — без поля «Марка»

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0003_product_brand"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="brand",
        ),
        migrations.AlterModelOptions(
            name="product",
            options={
                "ordering": ["category", "title"],
                "verbose_name": "Товар",
                "verbose_name_plural": "Товари",
            },
        ),
    ]
