from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class Profile(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     address = models.CharField(max_length=200)
#     phone = models.CharField(max_length=100)
#     image = models.ImageField(upload_to='Profile')

#     def __str__(self):
#         return f'{self.first_name} {self.last_name}'