from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pizza/', views.pizza, name='pizza'),
    path('trains/', views.trains, name='trains')
]