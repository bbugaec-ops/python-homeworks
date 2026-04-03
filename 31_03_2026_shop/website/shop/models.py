from django.db import models
from django.utils.text import slugify


class Product(models.Model):
    title = models.CharField(max_length=200, verbose_name='Назва')
    slug = models.SlugField(max_length=220, unique=True, db_index=True, blank=True)
    description = models.TextField(blank=True, verbose_name='Опис')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Ціна')
    image = models.ImageField(upload_to='shop/products', blank=True, null=True, verbose_name='Фото')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Створено')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товари'
        ordering = ['title']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.title) or 'product'
            s = base
            n = 1
            while Product.objects.filter(slug=s).exclude(pk=self.pk).exists():
                n += 1
                s = f'{base}-{n}'
            self.slug = s
        super().save(*args, **kwargs)
