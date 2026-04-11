from django.conf import settings
from django.db import models

from shop.models import Product


class Order(models.Model):
    STATUS_PENDING = "pending"
    STATUS_PAID = "paid"
    STATUS_SHIPPED = "shipped"
    STATUS_CANCELLED = "cancelled"
    STATUS_CHOICES = [
        (STATUS_PENDING, "В обробці"),
        (STATUS_PAID, "Оплачено"),
        (STATUS_SHIPPED, "Відправлено"),
        (STATUS_CANCELLED, "Скасовано"),
    ]

    order_number = models.CharField(
        max_length=32,
        unique=True,
        null=True,
        blank=True,
        editable=False,
        verbose_name="Номер замовлення",
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="orders",
        verbose_name="Користувач",
    )
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    address = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=5)
    city = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_PENDING,
        verbose_name="Статус",
    )

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Замовлення"
        verbose_name_plural = "Замовлення"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.order_number:
            num = f"ORD-{self.pk:08d}"
            Order.objects.filter(pk=self.pk).update(order_number=num)
            self.order_number = num

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

    def __str__(self):
        if self.order_number:
            return f"Замовлення {self.order_number}"
        return f"Замовлення #{self.pk}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="order_items", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = "Позиція замовлення"
        verbose_name_plural = "Позиції замовлень"

    def __str__(self):
        return f"{self.product_id} × {self.quantity}"

    def get_cost(self):
        return self.price * self.quantity
