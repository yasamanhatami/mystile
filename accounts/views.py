from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import SignUpForm
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