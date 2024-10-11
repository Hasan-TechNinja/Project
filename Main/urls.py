from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('shop/', views.ShopView.as_view(), name='shop'),  # Show all departments and products
    path('shop/<int:pk>/', views.ShopView.as_view(), name='shop_by_department'),  # Show products for a specific department
    path('product_details/', views.ProductDetails.as_view(), name='product_details'),
    path('product_details/<int:pk>/', views.ProductDetails.as_view(), name='product_details'),
    path('addtocart/', views.AddToCart, name = 'addtocart'),
    path('cart/', views.ShowCart, name="showcart"),
    path('checkout/', views.checkout, name='checkout'),
    path('departments/', views.DepartmentsView.as_view(), name='departments'),  # list view
    path('departments/<int:pk>/', views.DepartmentsView.as_view(), name='department_detail'),  # detail view
    path('cart/increase/<int:product_id>/', views.increase_cart_quantity, name='increase_cart_quantity'),
    path('cart/decrease/<int:product_id>/', views.decrease_cart_quantity, name='decrease_cart_quantity'),
    path('delete-cart/<int:cart_id>/', views.delete_cart_item, name='delete_cart_item'),
    path('blog/', views.BlogView, name='blog'),
    path('blogdetails/<int:pk>', views.BlogDetails.as_view(), name='blogdetails'),
    path('order/', views.OrderView, name='order'),
    path('search/', views.search, name='search'),

    
]
