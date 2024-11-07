from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import ProfileModel
from Main.models import Cart, Delivery, Billing_Details, WishList
from django.shortcuts import redirect
from .forms import ProfileForm
import json
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User


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



@login_required
def confirm_delete_profile(request):
    if request.method == "POST":
        data = json.loads(request.body)
        password = data.get("password")
        
        # Check if the provided password is correct
        user = authenticate(username=request.user.username, password=password)
        if user:
            # Password is correct; delete the user
            request.user.delete()
            logout(request)  # Log out the user after deletion
            return JsonResponse({"success": True})
        else:
            # Password is incorrect
            return JsonResponse({"success": False})
    
    return JsonResponse({"success": False}, status=400)

def account_deleted(request):
    return render(request, "account_deleted.html")  # Optional: Show a confirmation message
