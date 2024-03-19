from django.contrib import admin
from django.urls import path
from .views import user_form, product_form

urlpatterns = [
    path('user/add/', user_form, name='user_form'),
    path('product/add/', product_form, name='product_form'),
]
