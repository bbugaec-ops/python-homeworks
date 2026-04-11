from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from cart.cart import Cart

from .forms import OrderCreateForm
from .models import Order, OrderItem


@login_required
def order_create(request):
    cart = Cart(request)
    if request.method == "POST":
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item["product"],
                    price=item["price"],
                    quantity=item["quantity"],
                )
            cart.clear()
            messages.success(
                request,
                f"Замовлення {order.order_number} успішно оформлено. Дякуємо!",
            )
            return redirect("order:order_detail", pk=order.pk)
    else:
        form = OrderCreateForm()
    return render(request, "order/order_create.html", {"form": form, "cart": cart})


@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user).order_by("-created_at")
    return render(request, "order/my_orders.html", {"orders": orders})


@login_required
def order_detail(request, pk):
    order = get_object_or_404(
        Order.objects.prefetch_related("items__product"),
        pk=pk,
        user=request.user,
    )
    return render(request, "order/order_detail.html", {"order": order})
