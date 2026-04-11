import uuid

from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name="Назва")
    slug = models.SlugField(
        max_length=120,
        unique=True,
        db_index=True,
        blank=True,
        verbose_name="Slug (для URL)",
        help_text="Порожньо — згенерується латиницею; якщо назва лише кирилицею — буде технічний slug (c-…).",
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.name) or f"c-{uuid.uuid4().hex[:10]}"
            s = base
            n = 1
            while Category.objects.filter(slug=s).exclude(pk=self.pk).exists():
                n += 1
                s = f"{base}-{n}"
            self.slug = s
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"


class Product(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Опис")
    created_at = models.DateTimeField(auto_created=True, verbose_name="Дата публікації")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категорія")
    slug = models.SlugField(
        max_length=220,
        unique=True,
        db_index=True,
        blank=True,
        verbose_name="Slug (URL)",
        help_text="Порожньо — латиниця з заголовка; якщо лише кирилиця — технічний slug (p-…).",
    )
    image = models.ImageField(upload_to='shop/products')
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title) or f"p-{uuid.uuid4().hex[:10]}"
            slug = base_slug
            counter = 1
            while Product.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                counter += 1
                slug = f"{base_slug}-{counter}"
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товари"
