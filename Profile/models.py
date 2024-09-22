from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    about = models.CharField(default='Default about', max_length=300, null=True, blank=True)
    description = models.TextField(default='Default description', blank=True, null= True)
    address = models.CharField(max_length=200, null=True, blank=True)
    contact = models.CharField(max_length=100, null=True, blank=True)
    created = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    image = models.ImageField(default='/static/img/default.webp', upload_to='Profile', blank=True, null=True)

    def __str__(self):
        return f'{self.name}'