from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views import View
from . models import Product, Departments, Cart, BlogPost, Billing_Details, HomeCarousel
from . forms import BillingDetailsForm
from django.contrib.auth import authenticate
from django.utils.html import strip_tags

# Create your views here.

class HomeView(View):
    def get(self, request, *args, **kwargs):
        products = Product.objects.all()[:12:-1]
        departments = Departments.objects.all()
        blog = BlogPost.objects.all()[0:3:-1]
        Carousel = HomeCarousel.objects.all()
        
        context = {
            'products': products,
            'departments': departments,
            'blog':blog,
            'Carousel':Carousel
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
        quantity = product.stock
        if quantity < 1:
            stoke = "Stoke out!"
        else:
            stoke = quantity

        department_description = product.department.description
        all = Product.objects.all()
        
        related_products = Product.objects.filter(department=product.department).exclude(pk=pk)

        context = {
            'product': product,
            'stoke':stoke,
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
        departments = Departments.objects.all()
 
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

            context = {
                'departments': departments,
            }

        return render(request, 'departments.html', context)



    
def BlogView(request):
    data = BlogPost.objects.all()

    context = {
        'data':data
    }
    return render(request, 'blog.html', context)



class BlogDetails(View):
    def get(self, request, pk):
        Blog = get_object_or_404(BlogPost, pk=pk)
        category = Blog.category
        print(category)
        context = {
            'blog':Blog
        }
        return render(request, 'blogdetails.html', context)



@login_required
def checkout(request):
    cart = Cart.objects.filter(user=request.user)
    
    if request.method == 'POST':
        form = BillingDetailsForm(request.POST)
        
        if form.is_valid():
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            country = request.POST.get('country')
            division = request.POST.get('division')
            district = request.POST.get('district')
            thana = request.POST.get('thana')
            state = request.POST.get('state')
            zip_code = request.POST.get('zip_code')
            phone = request.POST.get('phone')
            second_phone = request.POST.get('second_phone')
            email = request.POST.get('email')
            user = request.user

            # Iterate through the cart and save billing details
            for c in cart:
                product = c.product  # Get the product from the cart item
                if product.stock >= c.quantity:
                    # Save billing details
                    Billing_Details.objects.create(
                        user=user,
                        first_name=first_name,
                        last_name=last_name,
                        country=country,
                        division=division,
                        district=district,
                        thana=thana,
                        state=state,
                        zip_code=zip_code,
                        phone=phone,
                        second_phone=second_phone,
                        email=email,
                        product=product,
                        quantity=c.quantity,
                    )

                    # Decrease product stock
                    product.stock -= c.quantity

                    # If stock is below 1, set stock to 0 and optionally mark product as "out of stock"
                    if product.stock < 1:
                        product.stock = 0  # Set stock to 0 if it's less than 1

                    product.save()  # Save the updated product stock

                    # Remove the item from the cart after placing the order
                    c.delete()

                else:
                    # Handle insufficient stock, show an error message (optional)
                    return render(request, 'checkout.html', {
                        'form': form,
                        'cart': cart,
                        'error': f'Not enough stock for {product.name}. Only {product.stock} left.'
                    })

            # After processing all items, redirect to home
            return redirect('home')

        else:
            # Handle form errors
            context = {'form': form}
            return render(request, 'checkout.html', context)

    else:
        form = BillingDetailsForm()

    context = {
        'form': form,
        'cart': cart
    }
    return render(request, 'checkout.html', context)




def OrderView(request):
    order = Billing_Details.objects.filter(user=request.user)
    order_product = [p for p in order]
    total = len(order)
    subtotal = 0  # Initialize the subtotal variable

    for p in order_product:
        if p.product:  # Check if product exists before calculating
            p.linetotal = p.quantity * p.product.selling_price  # Calculate line total
            subtotal += p.linetotal  # Add to subtotal
    address = f"{order.first().state}, {order.first().thana}, {order.first().district}, {order.first().division}, {order.first().country}"
    context = {
        'order': order,
        'subtotal': subtotal,
        'address': address,
        'total':total
    }
    return render(request, 'order.html', context)
