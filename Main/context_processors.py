from .models import About, Social, PaymentMethod, Cart
from Profile.models import ProfileModel
from datetime import datetime


def about_context(request):
    about = About.objects.first()
    year = datetime.now().year
    social = Social.objects.all()
    payment_method = PaymentMethod.objects.all()
    profile = None
    cart_item = 0

    if request.user.is_authenticated:
        profile = ProfileModel.objects.filter(user=request.user).first()
        cart = Cart.objects.filter(user=request.user)
        cart_item = cart.count()

    return {
        'about': about,
        'year': year,
        'social': social,
        'payment': payment_method,
        'profile': profile,
        'cart_item': cart_item,
    }