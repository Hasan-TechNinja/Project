from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from tinymce.models import HTMLField
from django.utils import timezone
from django.utils.text import slugify
from decimal import Decimal
from Profile.models import ProfileModel

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

class Brand(models.Model):
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=500)
    logo = models.ImageField(upload_to='brand', null=True, blank=True)  
    banner = models.ImageField(upload_to='brand', null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    discount_percentage = models.IntegerField(default=0)
    discount_price = models.DecimalField(max_digits=10, decimal_places=1, default=0)
    SpecialOffer_price = models.DecimalField(max_digits=10, decimal_places=1, default=0)
    stock = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    image1 = models.ImageField(upload_to='products/', blank=True, null=True)
    image2 = models.ImageField(upload_to='products/', blank=True, null=True)
    image3 = models.ImageField(upload_to='products/', blank=True, null=True)
    image4 = models.ImageField(upload_to='products/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='products', null=True)
    shipping_time = models.CharField(max_length=50, choices=[('1','1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default='3')
    selles = models.IntegerField(default=0)
    product_video = models.URLField(blank=True)
    department = models.ForeignKey(Departments, on_delete=models.CASCADE, related_name='products')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    size = models.ForeignKey(Size, on_delete=models.CASCADE, related_name='products', blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
    # Calculate discount price based on discount percentage before saving the product.
        if self.discount_percentage > 0:
            # Ensure the discount calculation uses Decimal to avoid type mismatch
            discount_factor = Decimal(self.discount_percentage) / Decimal(100)
            self.discount_price = self.selling_price * (1 - discount_factor)
        else:
            self.discount_price = self.selling_price
        super(Product, self).save(*args, **kwargs)
    

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    p_id = models.CharField(max_length=100,null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username}"
    
    def linetotal(self):
        return self.product.selling_price * self.quantity
    


class Billing_Details(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    p_id = models.CharField(max_length=100,null=True, blank=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    product=models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null= True)
    quantity=models.PositiveIntegerField(default=1)
    country = CountryField(blank_label='(select country)')
    division = models.CharField(max_length=255)
    district = models.CharField(max_length=100)
    thana = models.CharField(max_length=100)
    street = models.CharField(max_length=100, blank=True, null=True)
    zip_code = models.CharField(max_length=20, blank=True, null=True)
    phone = models.CharField(max_length=25)
    datetime = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    order_note = models.CharField(max_length=200, blank=True, null=True)
    second_phone = models.CharField(max_length=25, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)


    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.user.username})"
    
    def linetotal(self):
        return self.product.selling_price * self.quantity
    

class Delivery(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    p_id = models.CharField(max_length=100,null=True, blank=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    product=models.ForeignKey(Product, on_delete=models.CASCADE, related_name='delivery', blank=True, null= True)
    quantity=models.PositiveIntegerField(default=1)
    country = CountryField(blank_label='(select country)')
    division = models.CharField(max_length=255)
    district = models.CharField(max_length=100)
    thana = models.CharField(max_length=100)
    street = models.CharField(max_length=100, blank=True, null=True)
    zip_code = models.CharField(max_length=20, blank=True, null=True)
    phone = models.CharField(max_length=25)
    order_note = models.CharField(max_length=200, blank=True, null=True)
    datetime = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    second_phone = models.CharField(max_length=25, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    delivery_charge = models.DecimalField(max_digits=10, decimal_places=2, default=100.00)  # Add delivery charge

    def __str__(self):
        return f"{self.first_name} {self.last_name}, order"
    
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


class HomeCarousel(models.Model):
    name = models.CharField(max_length=300, blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    link = models.CharField(max_length=500, blank=True, null=True, default="#")
    banner = models.ImageField(upload_to='Project')

    def __str__(self):
        return self.name
    

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews")
    p_id = models.CharField(max_length=100, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=5)  # Rating between 1 and 5
    comment = models.TextField(max_length=500, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Review for {self.product.name} by {self.user.username}"
    
    class Meta:
        ordering = ['-created_at']
        unique_together = ('product', 'user')

class WishList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"
    
class Coupon(models.Model):
    code = models.CharField(max_length=15, unique=True)
    discount = models.DecimalField(max_digits=6, decimal_places=2, help_text="Discount in percentage (e.g.., 10 for 10%)")
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.code

    def is_valid(self):
        now = timezone.now()
        return self.active and self.valid_from <= now <= self.valid_to
    

class About(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True)
    about = models.CharField(max_length=300)
    description = models.TextField()
    contact = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mission_statement = models.CharField(max_length=255, blank=True)
    vision = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    logo = models.ImageField(upload_to='Project/', blank=True)
    banner = models.ImageField(upload_to='Project/')
    year_established = models.PositiveIntegerField(blank=True, null=True)
    support_contact = models.CharField(max_length=100, blank=True)
    operating_hours = models.CharField(max_length=100, blank=True)
    map_location = models.URLField(max_length=200, blank=True)
    testimonials = models.TextField(blank=True)
    team_info = models.TextField(blank=True)
    team_members = models.ManyToManyField(ProfileModel, blank=True, related_name='about_pages')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Social(models.Model):
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=400)
    logo = models.ImageField(upload_to='Project')

    def __str__(self):
        return self.name
    
class PaymentMethod(models.Model):
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=400)
    logo = models.ImageField(upload_to='Project')

    def __str__(self):
        return self.name
    

class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question
    


class SpecialOffer(models.Model):
    products = models.ManyToManyField(Product, related_name="special_offers")
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    discount_percentage = models.PositiveIntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    active = models.BooleanField(default=True)
    banner = models.ImageField(upload_to='Offer')

    def __str__(self):
        return self.title

    def is_active(self):
        """Check if the offer is currently active based on date."""
        now = timezone.now()
        return self.active and self.start_date <= now <= self.end_date

    def get_discounted_price(self, product):
        """
        Calculate the discounted price for a specific product in this offer.
        """
        if self.discount_percentage > 0 and product.selling_price:
            discount_factor = Decimal(self.discount_percentage) / Decimal(100)
            return product.selling_price * (1 - discount_factor)
        return product.selling_price
