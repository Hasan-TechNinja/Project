from django.shortcuts import render, get_object_or_404
from .models import ProfileModel

def Profile(request):
    # Get the profile for the logged-in user
    profile = get_object_or_404(ProfileModel, user=request.user)
    

    context = {
        'profile': profile
    }
    return render(request, 'profiles.html', context)
