from django.contrib import admin
from django.urls import path, include
from urlshortner import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('<str:pk>', views.go, name='go'),   # a dynamic url which take a string and stores it in pk
]