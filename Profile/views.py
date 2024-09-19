from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import ProfileModel
from django.shortcuts import redirect
from .forms import ProfileForm

@login_required(login_url='login')
def Profile(request):
    profile = get_object_or_404(ProfileModel, user=request.user)
    name = 'Your Name'
    if profile.first_name:
        name = str(profile.first_name + ' ' + profile.last_name)

    context = {
        'profile': profile,
        'name': name
    }
    return render(request, 'profile.html', context)


@login_required(login_url='login')
def EditProfile(request):
    profile = get_object_or_404(ProfileModel, user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)

    context = {
        'form': form,
        'profile':profile
    }
    return render(request, 'editprofile.html', context)