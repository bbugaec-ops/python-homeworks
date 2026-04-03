from . import views
from django.urls import path


urlpatterns = [
    path('', views.gallery_list, name="gallery"),
    path('upload/', views.upload, name="upload"),


    ]