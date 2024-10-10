from django import forms
from .models import Billing_Details, Review

class BillingDetailsForm(forms.ModelForm):
    class Meta:
        model = Billing_Details
        fields = ['first_name', 'last_name', 'country', 'division', 'district', 'thana', 'state', 'zip_code', 'phone', 'second_phone', 'email']

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:border-indigo-500 focus:ring-indigo-500', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:border-indigo-500 focus:ring-indigo-500', 'placeholder': 'Last Name'}),
            'country': forms.Select(attrs={'class': 'mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:border-indigo-500 focus:ring-indigo-500'}),
            'division': forms.TextInput(attrs={'class': 'mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:border-indigo-500 focus:ring-indigo-500', 'placeholder': 'Division'}),
            # 'product': forms.TextInput(attrs={'class': 'mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:border-indigo-500 focus:ring-indigo-500', 'placeholder': 'Product'}),
            # 'quantity': forms.TextInput(attrs={'class': 'mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:border-indigo-500 focus:ring-indigo-500', 'placeholder': 'Quantity'}),
            'district': forms.TextInput(attrs={'class': 'mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:border-indigo-500 focus:ring-indigo-500', 'placeholder': 'District'}),
            'thana': forms.TextInput(attrs={'class': 'mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:border-indigo-500 focus:ring-indigo-500', 'placeholder': 'Thana'}),
            'state': forms.TextInput(attrs={'class': 'mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:border-indigo-500 focus:ring-indigo-500', 'placeholder': 'State'}),
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
            'comment': forms.TextInput(attrs={'class': 'mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:border-indigo-500 focus:ring-indigo-500', 'placeholder': 'Comment'}),
        }