from django.shortcuts import render,redirect
from django.urls import reverse
from registration.forms import RegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
# from django.contrib.auth.decorators import login_required

# Create your views here.
def registration(request):
    # if request.method =='POST':
    #     form = RegistrationForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect(reverse('employee_manager/home.html'))
    # else:
    form = RegistrationForm()   
    args = {'form': form}
    return render(request, 'registration/reg_form.html',args)

def login(request):
    if 'text1' in request.GET:
        message = ' %r' % request.GET['text1']
    else:
        message = 'You submitted an empty form.'
    print(message)
    return render(request,'registration/login.html')

def TwoFactorAuthentication(request):
    print(request)
    return render(request,'registration/2FA.html')

def OTPAuthentication(request):

    return render(request,'registration/OTP_Auth.html')
