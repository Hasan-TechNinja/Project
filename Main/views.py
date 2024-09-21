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
        products = Product.objects.all()[:12:-1]
        departments = Departments.objects.all()
        context = {
            'products': products,
            'departments': departments,
        }
        return render(request, 'home.html', context) 
    

class ShopView(View):
    def get(self, request, pk=None):
        departments = Departments.objects.all()
        if pk:
            # Fetch products that belong to the selected department
            selected_department = get_object_or_404(Departments, pk=pk)
            products = Product.objects.filter(department=selected_department)  # Adjust this line as per your model
        else:
            # If no department is selected, show all products or handle as needed
            products = Product.objects.all()  # Show all products (or handle empty state)
        
        context = {
            'department': departments,
            'products': products
        }
        return render(request, 'shop.html', context)





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

@login_required(login_url='login')
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

@login_required(login_url='login')
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

@login_required(login_url='login')
def increase_cart_quantity(request, product_id):
    if request.user.is_authenticated:
        user = request.user
        cart_item = get_object_or_404(Cart, user=user, product_id=product_id)
        
        cart_item.quantity += 1
        cart_item.save()
        
        return redirect('showcart')  
    return redirect('login') 

@login_required(login_url='login')
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

@login_required(login_url='login')
def delete_cart_item(request, cart_id):
    cart_item = get_object_or_404(Cart, id=cart_id, user=request.user)
    cart_item.delete()
    return redirect('showcart')



class DepartmentsView(View, LoginRequiredMixin):
    def get(self, request, pk=None):
        # Fetch all departments (this will always be passed to the template)
        departments = Departments.objects.all()

        # If 'department_id' is in the query parameters or a pk is provided in the URL
        department_id = request.GET.get('department_id') or pk
        
        if department_id:
            # Get the department by 'department_id' or 'pk'
            department = get_object_or_404(Departments, pk=department_id)
            
            # Fetch related products for the selected department
            related_products = Product.objects.filter(department=department)

            context = {
                'department': department,   
                'rproduct': related_products, 
                'departments': departments,
            }
        else:
            # If no department is selected, show only the department list
            context = {
                'departments': departments,   # List of all departments (for sidebar/menu)
            }

        return render(request, 'departments.html', context)


    
def BlogView(request):
    data = Blog.objects.all()

    context = {
        'data':data
    }
    return render(request, 'blog.html', context)