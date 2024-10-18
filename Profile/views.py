from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import ProfileModel
from Main.models import Cart, Delivery, Billing_Details, WishList
from django.shortcuts import redirect
from .forms import ProfileForm

@login_required(login_url='login')
def Profile(request):
    user = request.user
    profile = get_object_or_404(ProfileModel, user = user)
    cart = Cart.objects.filter(user = user).order_by('-id')
    order = Billing_Details.objects.filter(user = user).order_by('-id')[0:3]

    name = 'Your Name'
    if profile.first_name:
        name = str(profile.first_name + ' ' + profile.last_name)

    address = Delivery.objects.filter(user=user).order_by('-id')[0:3]
    purchase = Delivery.objects.filter(user = user).order_by('-id')
    wishlist = WishList.objects.filter(user = user)

    context = {
        'profile': profile,
        'name': name,
        'cart': cart,
        'order':order,
        'address':address,
        'purchase':purchase,
        'wishlist':wishlist,
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