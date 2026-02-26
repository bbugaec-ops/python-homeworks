from django.conf.global_settings import STATIC_ROOT
from django.contrib import admin
from helloweb import views, homework_1
from  django.urls import path

from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('old-home/', views.index, name='home'),
    path('datetime/', views.current_datetime, name='datetime'),
    path('datetime_class/',views.CurrentDateTime.as_view()),
    path('citata/',views.citata,name='citata'),

    #-------------------------------------
    #-----перше завдання----------
    path('admin/', admin.site.urls),
    path('',homework_1.home),
    path('news/',homework_1.news),
    path('management/',homework_1.management),
    path('facts/',homework_1.facts),
    path('contacts/',homework_1.contacts),


    #------2 друге завдання----------------
    path('history/', homework_1.history),
    path('history/people/', homework_1.history_people),
    path('history/photos/', homework_1.history_photos),



]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)