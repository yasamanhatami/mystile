from django.shortcuts import render

# Create your views here.
def login_view(request):

    return render(request,'accounts/login.html')
#def logout_view(request):


def signup_view(request):
    return render (request,'accounts/signup.html')