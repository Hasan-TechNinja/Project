from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.


def Profile(request):
    user = request.user

    username = user.username
    first_name = user.first_name
    last_name = user.last_name

    full_name = f"{first_name} {last_name}"

    context = {
        'username': username,
        'first_name': first_name,
        'last_name': last_name,
        'full_name': full_name
    }

    return render(request, 'profile.html', context)