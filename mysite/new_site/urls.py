from django.urls import path
# Path is a functuion that is used to define a URl pattern; a URL pattern is a way of mapping a URL to a view.
from . import views
# A view is bassically just the page of a website; views are responsible for taking a request and giving the correct response back AKA going to diffrent screens.
urlpatterns = [
    path('', views.index, name='index'),
    path('pizza/', views.pizza, name='pizza'),
    path('trains/', views.trains, name='trains')  ##What ??
]
# This whole thing is just describing diffrent paths you can take on the website. So going to pizza/ gives the request for the pizza page.