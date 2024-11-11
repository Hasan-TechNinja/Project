from django import forms
from django.forms.models import ModelForm
from .models import ProfileModel

class ProfileForm(ModelForm):
    class Meta:
        model = ProfileModel
        fields = '__all__'
        exclude = ['user', 'status']

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        # Tailwind CSS classes for design
        self.fields['first_name'].widget.attrs.update({
            'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-blue-500 focus:border-blue-500',
            'placeholder': 'Enter your firstname',
        })

        self.fields['last_name'].widget.attrs.update({
            'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-blue-500 focus:border-blue-500',
            'placeholder': 'Enter your lastname',
        })
        
        self.fields['about'].widget.attrs.update({
            'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-blue-500 focus:border-blue-500',
            'placeholder': 'About your self',
        })
        
        self.fields['description'].widget.attrs.update({
            'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-blue-500 focus:border-blue-500',
            'placeholder': 'Enter a description',
        })

        self.fields['contact'].widget.attrs.update({
            'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-blue-500 focus:border-blue-500',
            'placeholder': 'Enter your phone number',
        })

        self.fields['address'].widget.attrs.update({
            'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-blue-500 focus:border-blue-500',
            'placeholder': 'Enter your address',
        })

        self.fields['facebook'].widget.attrs.update({
            'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-blue-500 focus:border-blue-500',
            'placeholder': 'Enter your facebook url',
        })

        self.fields['instagram'].widget.attrs.update({
            'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-blue-500 focus:border-blue-500',
            'placeholder': 'Enter your instagram url',
        })

        self.fields['linkedin'].widget.attrs.update({
            'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-blue-500 focus:border-blue-500',
            'placeholder': 'Enter your LinkedIn url',
        })

        self.fields['twitter'].widget.attrs.update({
            'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-blue-500 focus:border-blue-500',
            'placeholder': 'Enter your Twitter url',
        })

        self.fields['whatsapp'].widget.attrs.update({
            'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-blue-500 focus:border-blue-500',
            'placeholder': 'Enter your WhatsApp number',
        })

        # self.fields['telegram'].widget.attrs.update({
        #     'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-blue-500 focus:border-blue-500',
        #     'placeholder': 'Enter your Telegram number',
        # })

        self.fields['github'].widget.attrs.update({
            'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-blue-500 focus:border-blue-500',
            'placeholder': 'Enter your Github url',
        })

        # Custom file input for image upload
        self.fields['image'].widget.attrs.update({
            'class': 'block w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-lg file:border-0 file:text-sm file:font-semibold file:bg-blue-600 file:text-white hover:file:bg-blue-700',
        })
