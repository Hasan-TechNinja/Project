from django.contrib import admin
from .models import Profile

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'name', 'title', 'description', 'address', 'contact', 'image'
    )

admin.site.register(Profile, ProfileAdmin)