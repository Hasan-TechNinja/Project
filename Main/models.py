from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from tinymce.models import HTMLField
from django.utils import timezone
from django.utils.text import slugify

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
    


class Billing_Details(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    product=models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null= True)
    quantity=models.PositiveIntegerField(default=1)
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
    
    def linetotal(self):
        return self.product.selling_price * self.quantity
    




class BlogPost(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    slug = models.SlugField(unique=True, max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = HTMLField()
    featured_image = models.ImageField(upload_to='Blogs/')
    tags = models.ManyToManyField('Tag', blank=True)  # Assuming 'Tag' is defined elsewhere
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)  # Assuming 'Category' is defined elsewhere
    excerpt = models.CharField(max_length=500, blank=True)
    publish_date = models.DateTimeField(default=timezone.now)  # Default to now
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=[('draft', 'Draft'), ('published', 'Published')], default='draft')
    views = models.IntegerField(default=0)
    meta_title = models.CharField(max_length=70, blank=True)
    meta_description = models.CharField(max_length=160, blank=True)
    comments_enabled = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
