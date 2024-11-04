from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.AboutView, name='about'),
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
    path('orders/', views.OrderView, name='orders_page'),
    path('order/<int:order_id>/deliver/', views.DeliveryView, name='delivery'),
    path('order/<int:order_id>/cancel/', views.cancel_order, name='cancel_order'),
    path('purchase/', views.Purchase, name='purchase'),
    path('search/', views.search, name='search'),
    # path('review/', views.ProductReview, name='review'),
    path('review/<str:p_id>/', views.ProductReviewView.as_view(), name='review'),
    path('wishlist', views.wishlist_view, name='wishlist'),
    path('wishlist/add/<int:product_id>',views.add_to_wishlist , name='add_to_wishlist'),
    path('wishlist/remove/<int:product_id>', views.remove_from_wishlist, name='remove_from_wishlist'),
    path('faq/', views.faq_view, name='faq'),
    path('special-offers/<int:offer_id>/', views.offer_details, name='offer_details'),
    # path('offer-product-details/', views.OfferProductDetails.as_view(), name='offerPdetails'),
    # path('offer-product-details/<int:pk>/', views.OfferProductDetails.as_view(), name='offerPdetails'),


]
