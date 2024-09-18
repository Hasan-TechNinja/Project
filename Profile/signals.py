# from .models import Profile
# from django.contrib.auth.models import User

# from django.db.models.signals import post_save
# from django.dispatch import receiver


# @receiver(post_save, sender = User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         created = Profile.objects.get_or_create(user = instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()


from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import ProfileModel  # Ensure you are importing the correct model
from django.contrib.auth.models import User

# Automatically create a ProfileModel when a User is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        ProfileModel.objects.get_or_create(user=instance)

# Save the ProfileModel when the User object is saved
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    # Save the associated ProfileModel
    instance.profilemodel.save()
