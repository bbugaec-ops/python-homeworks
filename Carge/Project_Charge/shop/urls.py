from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from .forms import ChargeAuthenticationForm

urlpatterns = [
    path("", views.home, name="home"),
    path("accounts/register/", views.signup, name="register"),
    path(
        "accounts/login/",
        auth_views.LoginView.as_view(
            template_name="shop/login.html",
            authentication_form=ChargeAuthenticationForm,
        ),
        name="login",
    ),
    path(
        "accounts/logout/",
        auth_views.LogoutView.as_view(),
        name="logout",
    ),
    path(
        "catalog/category/<int:category_id>/",
        views.product_list,
        name="product_list_category",
    ),
    path("catalog/", views.product_list, name="product_list"),
    path("product/<str:slug>/", views.product_detail, name="product_detail"),
    path("cart/", views.cart_view, name="cart"),
    path("cart/update/", views.cart_update, name="cart_update"),
    path("cart/inc/<int:pk>/", views.cart_increment, name="cart_increment"),
    path("cart/dec/<int:pk>/", views.cart_decrement, name="cart_decrement"),
    path("cart/add/<str:slug>/", views.cart_add, name="cart_add"),
    path("cart/remove/<int:pk>/", views.cart_remove, name="cart_remove"),
    path("order/create/", views.order_create, name="order_create"),
]
