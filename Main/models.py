from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    link = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='Category logo', blank=True, null=True )

    def __str__(self):
        return self.name


class Departments(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank= True, null=True)
    link = models.CharField(max_length=500)
    image = models.ImageField(upload_to='departments', blank=True, null=True)

    def __str__(self):
        return self.name


class Size(models.Model):
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=500)

    def __str__(self):
        return self.name



class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    stock = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    image1 = models.ImageField(upload_to='products/', blank=True, null=True)
    image2 = models.ImageField(upload_to='products/', blank=True, null=True)
    image3 = models.ImageField(upload_to='products/', blank=True, null=True)
    image4 = models.ImageField(upload_to='products/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    department = models.ForeignKey(Departments, on_delete=models.CASCADE, related_name='products')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    size = models.ForeignKey(Size, on_delete=models.CASCADE, related_name='products', blank=True, null=True)

    def __str__(self):
        return self.name
    

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.user.username}"
    
    def linetotal(self):
        return self.product.selling_price * self.quantity
    

class Blog(models.Model):
    title = models.CharField(max_length=100)
    about = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    comment = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='Blog')

    def __str__(self):
        return self.title
    

class Billing_Details(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    country = CountryField(blank_label='(select country)')
    division = models.CharField(max_length=255)
    district = models.CharField(max_length=100)
    thana = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20, blank=True, null=True)
    phone = models.CharField(max_length=25)
    second_phone = models.CharField(max_length=25, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.user.username})"