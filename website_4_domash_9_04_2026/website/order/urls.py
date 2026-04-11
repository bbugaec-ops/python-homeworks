from django.urls import path

from . import views

app_name = "order"

urlpatterns = [
    path("create/", views.order_create, name="order_create"),
    path("mine/", views.my_orders, name="order_list"),
    path("<int:pk>/", views.order_detail, name="order_detail"),
]
