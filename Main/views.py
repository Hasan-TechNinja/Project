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

class ProductDetails(View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        department_description = product.department.description 
        
        all = Product.objects.all()
        related_products = Product.objects.filter(department=product.department).exclude(pk=pk)

        context = {
            'product': product,
            'rproduct':related_products,
            'department_description':department_description,

        }
        return render(request, 'product_details.html', context)

class AddToCart(LoginRequiredMixin ,View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request):

        return render(request, 'addtocart.html')