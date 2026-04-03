from . import views
from django.urls import path
from django.views.generic import RedirectView

urlpatterns = [
    path('', views.index, name="home"),
    path('Home/', RedirectView.as_view(url='/', permanent=False)),
    path('contacts/', views.contacts, name="contacts"),
    path('post/<slug:slug>', views.post_detail, name="post_detail"),
    path('category/<slug:slug>', views.category, name="category"),
    path('tag/<slug:slug>', views.tag_posts, name="tag"),
    path('search/', views.search, name="search"),
    path('create-post/', views.create_post, name="create_post"),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
]
