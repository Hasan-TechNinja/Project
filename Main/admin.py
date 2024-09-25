from django.contrib import admin
from . models import Product, Departments, Category, Size, Cart, Blog, Billing_Details

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

class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'about',
        'description',
        'date',
        'comment',
        'image'
    )
admin.site.register(Blog, BlogAdmin)


class Billing_DetailsAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'first_name',
        'last_name',
        'country',
        'division',
        'district',
        'thana',
        'state',
        'zip_code',
        'phone',
        'second_phone',
        'email'
    )

admin.site.register(Billing_Details, Billing_DetailsAdmin)