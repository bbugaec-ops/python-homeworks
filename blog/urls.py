from django.urls import path
from . import views

urlpatterns = [
    # Наприклад, головна сторінка блогу
    path('', views.index, name='blog_index'),
    path('contacts/', views.contacts, name='contacts'),
    path('football/', views.football, name='football'),
    path('hokey/', views.hokey, name='hokey'),
    path('basketball/', views.basketball, name='basketball'),


    #--------------------------#
    path('toyota/', views.toyota, name='toyota'),
    path('honda/', views.honda, name='honda'),
    path('renault/', views.renault, name='renault'),

    #-----------------------------------

    path('day/', views.day_style, name='day_style'),
]