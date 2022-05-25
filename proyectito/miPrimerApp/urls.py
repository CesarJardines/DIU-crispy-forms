from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings


app_name = "miPrimerApp"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('registro/', views.registro, name = 'registro'),
    path('home/', views.home, name = 'home'),

]

