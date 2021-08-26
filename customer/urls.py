from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('product/', views.Product, name='Product'),
    path('Customer/<str:pk_test>/', views.Customer, name="Customer"),
    path('create_order/', views.createOrder, name="create_order"),
    path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),


]