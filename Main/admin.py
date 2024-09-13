from django.contrib import admin
from . models import Product, Departments, Category, Size, Cart

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