from django.contrib import admin

from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ("product", "price", "quantity")


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        "order_number",
        "user",
        "first_name",
        "second_name",
        "email",
        "phone",
        "status",
        "created_at",
        "total_cost_display",
    ]
    list_filter = ["status", "created_at"]
    list_editable = ["status"]
    search_fields = [
        "order_number",
        "email",
        "phone",
        "first_name",
        "second_name",
        "user__username",
    ]
    readonly_fields = ["order_number", "created_at"]
    inlines = [OrderItemInline]

    @admin.display(description="Сума")
    def total_cost_display(self, obj):
        return obj.get_total_cost()


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ["order", "product", "price", "quantity"]
