from django.contrib import admin
from . models import Product, Departments, Category, Size

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
        'created_at', 
        'updated_at', 
        'department', 
        'category', 
        'size'
    )

admin.site.register(Product, ProductAdmin)
