import os
import uuid
from django.db import models
from django import forms
from django.utils.text import slugify



def product_image_upload_to(instance, filename):
    ext = os.path.splitext(filename)[1].lower()
    if ext not in (".jpg", ".jpeg", ".png", ".gif", ".webp", ".bmp"):
        ext = ".jpg"
    return f"products/{uuid.uuid4().hex}{ext}"



class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва")
    slug = models.SlugField(max_length=120, unique=True, blank=True, verbose_name="Slug (для URL)")

    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=200, verbose_name="Назва")
    slug = models.SlugField(max_length=220, unique=True, blank=True, verbose_name="Slug (для URL)")
    description = models.TextField(blank=True, verbose_name="Опис")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products", verbose_name="Категорія")
    image = models.ImageField(upload_to=product_image_upload_to, max_length=255, blank=True, null=True, verbose_name="Фото")

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товари"
        ordering = ["category", "title"]

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.title, allow_unicode=True) or slugify(self.title) or 'product'
            s = base
            n = 1
            while Product.objects.filter(slug=s).exclude(pk=self.pk).exists():
                n += 1
                s = f'{base}-{n}'
            self.slug = s
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title



class Order(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="Ім'я")
    last_name = models.CharField(max_length=50, verbose_name="Прізвище")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    address = models.CharField(max_length=250, verbose_name="Адреса доставки")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата замовлення")
    paid = models.BooleanField(default=False, verbose_name="Оплачено")

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Замовлення'
        verbose_name_plural = 'Замовлення'

    def __str__(self):
        return f'Замовлення №{self.id}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна на момент покупки")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Кількість")

    def __str__(self):
        return f'Товар {self.product.title} до замовлення {self.order.id}'



class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'phone', 'address']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'placeholder': 'Ваше ім\'я'})
        self.fields['last_name'].widget.attrs.update({'placeholder': 'Ваше прізвище'})
        self.fields['phone'].widget.attrs.update({'placeholder': '+380.....'})
        self.fields['address'].widget.attrs.update({'placeholder': 'Місто, відділення Нової Пошти....'})