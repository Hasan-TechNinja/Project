from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('shop/', views.ShopView, name='shop'),
    path('product_details', views.ProductDetails, name='product_details'),
    
]
