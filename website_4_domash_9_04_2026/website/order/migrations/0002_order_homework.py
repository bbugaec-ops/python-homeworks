import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


def copy_paid_status_and_numbers(apps, schema_editor):
    Order = apps.get_model("order", "Order")
    for o in Order.objects.order_by("pk"):
        paid = getattr(o, "paid", False)
        status = "paid" if paid else "pending"
        num = f"ORD-{o.pk:08d}"
        Order.objects.filter(pk=o.pk).update(status=status, order_number=num)


def noop(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("order", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="order",
            old_name="created",
            new_name="created_at",
        ),
        migrations.AlterModelOptions(
            name="order",
            options={
                "ordering": ["-created_at"],
                "verbose_name": "Замовлення",
                "verbose_name_plural": "Замовлення",
            },
        ),
        migrations.AddField(
            model_name="order",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="orders",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Користувач",
            ),
        ),
        migrations.AddField(
            model_name="order",
            name="status",
            field=models.CharField(
                choices=[
                    ("pending", "В обробці"),
                    ("paid", "Оплачено"),
                    ("shipped", "Відправлено"),
                    ("cancelled", "Скасовано"),
                ],
                default="pending",
                max_length=20,
                verbose_name="Статус",
            ),
        ),
        migrations.AddField(
            model_name="order",
            name="order_number",
            field=models.CharField(
                blank=True,
                editable=False,
                max_length=32,
                null=True,
                unique=True,
                verbose_name="Номер замовлення",
            ),
        ),
        migrations.RunPython(copy_paid_status_and_numbers, noop),
        migrations.RemoveField(
            model_name="order",
            name="paid",
        ),
        migrations.AlterModelOptions(
            name="orderitem",
            options={
                "verbose_name": "Позиція замовлення",
                "verbose_name_plural": "Позиції замовлень",
            },
        ),
    ]
