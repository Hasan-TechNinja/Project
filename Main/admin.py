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