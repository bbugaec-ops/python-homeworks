from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("order", "0002_order_homework"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="phone",
            field=models.CharField(default="", max_length=20, verbose_name="Телефон"),
            preserve_default=False,
        ),
    ]
