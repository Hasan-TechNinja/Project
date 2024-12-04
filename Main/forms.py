from django import forms
from .models import Billing_Details, Review, Coupon, Contact

class BillingDetailsForm(forms.ModelForm):
    class Meta:
        model = Billing_Details
        fields = ['first_name', 'last_name', 'country', 'division', 'district', 'thana', 'street', 'zip_code', 'phone', 'second_phone', 'email', 'order_note']

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:border-indigo-500 focus:ring-indigo-500', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:border-indigo-500 focus:ring-indigo-500', 'placeholder': 'Last Name'}),
            'country': forms.Select(attrs={'class': 'mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:border-indigo-500 focus:ring-indigo-500'}),
            'division': forms.TextInput(attrs={'class': 'mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:border-indigo-500 focus:ring-indigo-500', 'placeholder': 'Division'}),
            # 'product': forms.TextInput(attrs={'class': 'mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:border-indigo-500 focus:ring-indigo-500', 'placeholder': 'Product'}),
            # 'quantity': forms.TextInput(attrs={'class': 'mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:border-indigo-500 focus:ring-indigo-500', 'placeholder': 'Quantity'}),
            'district': forms.TextInput(attrs={'class': 'mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:border-indigo-500 focus:ring-indigo-500', 'placeholder': 'District'}),
            'thana': forms.TextInput(attrs={'class': 'mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:border-indigo-500 focus:ring-indigo-500', 'placeholder': 'Thana'}),
            'order_note': forms.TextInput(attrs={'class': 'mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:border-indigo-500 focus:ring-indigo-500', 'placeholder': 'Thana'}),
            'street': forms.TextInput(attrs={'class': 'mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:border-indigo-500 focus:ring-indigo-500', 'placeholder': 'State'}),
            'zip_code': forms.TextInput(attrs={'class': 'mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:border-indigo-500 focus:ring-indigo-500', 'placeholder': 'Zip Code'}),
            'phone': forms.TextInput(attrs={'class': 'mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:border-indigo-500 focus:ring-indigo-500', 'placeholder': 'Phone'}),
            'second_phone': forms.TextInput(attrs={'class': 'mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:border-indigo-500 focus:ring-indigo-500', 'placeholder': 'Second Phone (optional)'}),
            'email': forms.EmailInput(attrs={'class': 'mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:border-indigo-500 focus:ring-indigo-500', 'placeholder': 'Email'}),
        }



class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.TextInput(attrs={'class': 'mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:border-indigo-500 focus:ring-indigo-500', 'placeholder': 'Rating'}),
            'comment': forms.Textarea(attrs={'class': 'mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:border-indigo-500 focus:ring-indigo-500','placeholder': 'Comment','rows': 5,})

        }
class CouponForm(forms.Form):
    code = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={
            'class': 'mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:border-indigo-500 focus:ring-indigo-500', 
            'placeholder': 'Enter your coupon code'
        })
    )


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'order_number', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control block w-full px-4 py-2 border rounded-lg text-gray-800 placeholder-gray-400 bg-blue-50', 'placeholder':'Enter your name..'}),
            'email': forms.EmailInput(attrs={'class': 'form-control block w-full px-4 py-2 border rounded-lg text-gray-800 placeholder-gray-400 bg-blue-50', 'placeholder':'Enter your email..'}),
            'order_number': forms.TextInput(attrs={'class': 'form-control block w-full px-4 py-2 border rounded-lg text-gray-800 placeholder-gray-400 bg-blue-50', 'placeholder':'Enter order number'}),
            'message': forms.Textarea(attrs={'class': 'form-control block w-full px-4 py-2 border rounded-lg text-gray-800 placeholder-gray-400 bg-blue-50', 'placeholder':'Enter your message here..'}),
        }
