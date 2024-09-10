from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
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

class ProductDetails(LoginRequiredMixin, View):

    login_url = '/login/'  # Redirects to login page if not logged in
    redirect_field_name = 'redirect_to'


    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        all = Product.objects.all()
        rproduct = Product.objects.filter(department=product.department).exclude(pk=pk)

        context = {
            'product': product,
            'rproduct':rproduct,

        }
        return render(request, 'product_details.html', context)
