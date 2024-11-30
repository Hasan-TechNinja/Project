from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from . forms import CustomAuthenticationForm, CustomUserCreationForm, EmailVerificationForm, CustomPasswordChangeForm
from django.contrib import messages
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import EmailVerification

# Create your views here.

def RegistrationView(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Save the verification code in EmailVerification model
            verification = EmailVerification(user=user, code=form.email_verification_code)
            verification.save()

            return redirect('verify_email')  # Redirect to email verification page
    else:
        form = CustomUserCreationForm()

    context = {
        'form': form
    }
    return render(request, 'registration.html', context)



def VerifyEmailView(request):
    if request.method == 'POST':
        form = EmailVerificationForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            verification = get_object_or_404(EmailVerification, code=code)

            # Activate the user's account
            verification.user.is_active = True
            verification.user.save()

            # Delete the verification record after successful verification
            verification.delete()

            # login(request, verification.user)  # Log the user in after verification
            return redirect('login')
    else:
        form = EmailVerificationForm()

    context = {
        'form': form
    }
    return render(request, 'verify_email.html', context)






def LoginView(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('home')
        else:
            messages.error(request, "Login failed. Please check your username and password.")
    else:
        form = CustomAuthenticationForm()

    context = {
        'form':form
    }
    return render(request, 'login.html', context)



class CustomPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    form_class = CustomPasswordChangeForm
    template_name = 'password_change.html'
    success_url = reverse_lazy('password_change_done')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.user.username
        return context

class CustomPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = 'password_change_done.html'



def LogoutView(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('home')