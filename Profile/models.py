from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(default='Hasan', max_length=100, null=True, blank=True)
    title = models.CharField(default='This is the default, title change it in profile', max_length=300, null=True, blank=True)
    description = models.TextField(blank=True, null= True)
    address = models.CharField(max_length=200, null=True, blank=True)
    contact = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(default='img/default.webp' ,upload_to='Profile', blank=True, null=True)

    def __str__(self):
        return f'{self.name}'