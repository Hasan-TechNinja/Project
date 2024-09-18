from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views import View
from . models import Product, Departments, Cart, Blog
from django.contrib.auth import authenticate

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


def AddToCart(request):
    if request.user.is_authenticated:
        user = request.user
        product_id = request.GET.get("prod_id")
        product_quantity = int(request.GET.get("product_quantity", 1)) 
        product = Product.objects.get(id=product_id)

       
        try:
            cart_item = Cart.objects.get(user=user, product=product)
            cart_item.quantity = product_quantity
            cart_item.save()
        
        except Cart.DoesNotExist:
            Cart.objects.create(user=user, product=product, quantity=product_quantity)

       
        return redirect("/cart")
    
   
    return redirect("/authentication/login/")


def ShowCart(request):
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=user).order_by('-id')
        
        subtotal = 0 
        cart_product = [p for p in cart] 

        if cart_product: 
            
            for p in cart_product:
                p.linetotal = p.quantity * p.product.selling_price  
                subtotal += p.linetotal  

            return render(request, "addtocart.html", {'cart': cart, 'subtotal': subtotal}
            )
        else:
            return render(request, 'addtocart.html', {'cart': cart, 'subtotal': subtotal})
        
    return redirect('/cart')


def increase_cart_quantity(request, product_id):
    if request.user.is_authenticated:
        user = request.user
        cart_item = get_object_or_404(Cart, user=user, product_id=product_id)
        
        cart_item.quantity += 1
        cart_item.save()
        
        return redirect('showcart')  
    return redirect('login') 


def decrease_cart_quantity(request, product_id):
    if request.user.is_authenticated:
        user = request.user
        cart_item = get_object_or_404(Cart, user=user, product_id=product_id)
        
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
        
            cart_item.delete()
        
        return redirect('showcart')  
    return redirect('login') 

@login_required
def delete_cart_item(request, cart_id):
    cart_item = get_object_or_404(Cart, id=cart_id, user=request.user)
    cart_item.delete()
    return redirect('showcart')

    
    
class DepartmentsView(View):
    def get(self, request, pk):
        department = get_object_or_404(Departments, pk=pk)
        all = Departments.objects.all()
        
        related_products = Product.objects.filter(department=department.Departments.name).exclude(pk=pk)

        context = {
            'department': department,
            'rproduct':related_products,
            
        }
        return render(request, 'departments.html', context)
    
def BlogView(request):
    data = Blog.objects.all()

    context = {
        'data':data
    }
    return render(request, 'blog.html', context)