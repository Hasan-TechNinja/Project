# from django.shortcuts import render
# from django.contrib.auth.models import User

# # Create your views here.


# def Profile(request):


#     return render(request, 'profile.html')


from django.shortcuts import render, get_object_or_404
from .models import ProfileModel

def Profile(request):
    # Get the profile for the logged-in user
    profile = get_object_or_404(ProfileModel, user=request.user)
    
    # Pass the profile to the template
    context = {
        'profile': profile
    }
    return render(request, 'profile.html', context)
