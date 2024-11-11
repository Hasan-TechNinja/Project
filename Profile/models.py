from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ProfileModel(models.Model):
    STATUS_CHOICES = [
        ('Admin', 'Admin'),
        ('Manager', 'Manager'),
        ('Staff', 'Staff'),
        ('Employee', 'Employee'),
        ('Intern', 'Intern'),
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
        ('On Leave', 'On Leave'),
        ('Retired', 'Retired'),
        ('Junior Staff', 'Junior Staff'),
        ('Senior Staff', 'Senior Staff'),
        ('Lead', 'Lead'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    about = models.CharField(default='Default about', max_length=300, null=True, blank=True)
    description = models.TextField(default='Default description', blank=True, null= True)
    address = models.CharField(max_length=200, null=True, blank=True)
    contact = models.CharField(max_length=100, null=True, blank=True)
    created = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    image = models.ImageField(default='/static/img/default.webp', upload_to='Profile', blank=True, null=True)
    facebook = models.CharField(max_length=300, blank=True, null=True)
    instagram = models.CharField(max_length=300, blank=True, null=True)
    linkedin = models.CharField(max_length=300, blank=True, null=True)
    twitter = models.CharField(max_length=300, blank=True, null=True)
    whatsapp = models.CharField(max_length=200, blank=True, null=True)
    # telegram = models.CharField(max_length=200, blank=True, null=True)
    github = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Staff')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'