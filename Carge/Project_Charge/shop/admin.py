from django.contrib import admin

from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "price", "slug")
    list_filter = ("category",)
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "description")

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        f = form.base_fields.get("slug")
        if f:
            f.help_text = (
                "Можна лишити порожнім — після «Зберегти» заповниться з назви. "
                "Якщо з поля «Назва» slug не підставляється автоматично, "
                "увімкни JavaScript або введи короткий латинський slug вручну."
            )
        return form
    fieldsets = (
        (None, {"fields": ("title", "slug", "category", "price")}),
        ("Опис і фото", {"fields": ("description", "image")}),
    )
