from django.contrib import admin
from .models import ProfileModel

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'name', 'title', 'description', 'address', 'contact', 'created', 'image'
    )

admin.site.register(ProfileModel, ProfileAdmin)