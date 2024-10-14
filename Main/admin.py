from django.contrib import admin
from . models import Product, Departments, Category, Size, Cart, BlogPost, Billing_Details, Delivery, Brand, HomeCarousel, Review

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id', 
        'name', 
        'description', 
        'selling_price', 
        'discount_price', 
        'stock',
        'image',
        'image1',
        'image2',
        'image3',
        'image4',
        'created_at', 
        'updated_at', 
        'department', 
        'category', 
        'size'
    )

admin.site.register(Product, ProductAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'link',
        'image'
    )
admin.site.register(Category, CategoryAdmin)


class DepartmentsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'description',
        'link',
        'image'
    )
admin.site.register(Departments, DepartmentsAdmin)


class SizeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'link'
    )
admin.site.register(Size, SizeAdmin)


class CartAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user', 'product','quantity',
    )

admin.site.register(Cart, CartAdmin)

class BlogPostAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'slug',
        'author',
        'content',
        'featured_image',
        # 'tags',
        'category',
        'excerpt',
        'publish_date',
        'updated_at',
        'status',
        'views',
        'meta_title',
        'meta_description',
        'comments_enabled'
    )
admin.site.register(BlogPost, BlogPostAdmin)


class Billing_DetailsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'first_name',
        'last_name',
        'product',
        'quantity',
        'country',
        'division',
        'district',
        'thana',
        'street',
        'zip_code',
        'phone',
        'second_phone',
        'order_note',
        'datetime',
        'email'
    )

admin.site.register(Billing_Details, Billing_DetailsAdmin)


class DeliveryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'first_name',
        'last_name',
        'product',
        'quantity',
        'country',
        'division',
        'district',
        'thana',
        'street',
        'zip_code',
        'phone',
        'second_phone',
        'order_note',
        'datetime',
        'email'
    )

admin.site.register(Delivery, DeliveryAdmin)


class BrandAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'link',
        'logo',
        'banner'
    )
admin.site.register(Brand, BrandAdmin)


class HomeCarouselAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'title',
        'description',
        'link',
        'banner'
    )
admin.site.register(HomeCarousel, HomeCarouselAdmin)


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'user',
        'rating',
        'comment',
        'created_at',
        'updated_at'
    )
admin.site.register(Review, ReviewAdmin)