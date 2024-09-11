from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('shop/', views.ShopView, name='shop'),
    path('product_details/', views.ProductDetails.as_view(), name='product_details'),
    path('product_details/<int:pk>/', views.ProductDetails.as_view(), name='product_details'),
    # path('addtocart/', views.AddToCart.as_view(), name='addtocart'),
    path('addtocart/', views.AddToCart, name = 'addtocart'),
    path('cart/', views.show_cart, name="showcart"),
    # path('cart/', views.show_cart, name="showcart"),
    path('departments/', views.DepartmentsView.as_view(), name = 'departments'),
    # path('departments/<slug:pk>', views.DepartmentsView.as_view(), name = 'departments'),

    
]
