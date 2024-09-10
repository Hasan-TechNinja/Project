from django.shortcuts import render
from django.views import View
from . models import Product, Departments

# Create your views here.

class HomeView(View):
    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        departments = Departments.objects.all()
        context = {
            'products': products,
            'departments': departments,
        }
        return render(request, 'home.html', context) 

def ShopView(request):
    
    return render(request, 'shop.html')

def ProductDetails(request):
    return render(request, 'product_details.html')