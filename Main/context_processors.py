from .models import About, Social, PaymentMethod
from datetime import datetime

def about_context(request):
    about = About.objects.first()
    year = datetime.now().year
    social = Social.objects.all()
    payment_method = PaymentMethod.objects.all()

    return {'about': about, 'year': year, 'social':social, 'payment':payment_method,}
