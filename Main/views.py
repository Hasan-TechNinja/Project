from django.shortcuts import render

# Create your views here.

def HomeView(request):
    
    return render(request, 'home.html')

def ShopView(request):
    return render(request, 'shop.html')