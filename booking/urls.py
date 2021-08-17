from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('categories', views.tables, name='table'),
    path('price', views.price, name='price'),
    path('contact', views.contact, name='contact'),
]