from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import SignUpForm
#from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import (PasswordResetCompleteView,PasswordResetConfirmView,PasswordResetDoneView,PasswordResetView)
# Create your views here.
def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            input = request.POST['username']
            try:
                username = User.objects.get(email=input).username
            except User.DoesNotExist:
                username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                messages.add_message(request,messages.SUCCESS,'Login was successful')

                return redirect('/')
            else:
                messages.add_message(request,messages.ERROR,'The desired person was not found')
                return render(request, "accounts/login.html")
        form = AuthenticationForm()
        context = {'form': form}
        return render(request,'accounts/login.html',context)
    else:
        return redirect('/')
@login_required
def logout_view(request):
    logout(request)
    return redirect('/')


def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form=SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
        form=SignUpForm()
        context = {'form': form}
        return render (request,'accounts/signup.html',context)
    return redirect('/')
'''
class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'registration/password_reset.html'
    email_template_name = 'registration/password_reset_email.html'
    subject_template_name = 'registration/password_reset_subject.txt'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('registration:password_reset_done')
'''
class PasswordReset(PasswordResetView):
    template_name="registration/password_reset_form.html"
    success_url=reverse_lazy("accounts:password_reset_done")

class PasswordResetDone(PasswordResetDoneView):
    template_name="registration/password_reset_done.html"
    success_url=reverse_lazy("accounts:password_reset_confirm")

class PasswordResetConfirm(PasswordResetConfirmView):
    template_name="registration/password_reset_confirm.html"
    success_url=reverse_lazy("accounts:password_reset_complete")

class PasswordResetComplete(PasswordResetCompleteView):
    template_name="registration/password_reset_complete.html"