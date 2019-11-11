from django.shortcuts import render,redirect
from django.urls import reverse
from registration.forms import RegistrationForm
from django.contrib.auth.models import User,auth
from django.contrib import messages
# from django.contrib.auth.decorators import login_required

def registration(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('employee_manager:home'))
    else:
        form = RegistrationForm()
    args = {'form':form}
    return render(request,'registration/reg_form.html',args)
        
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('registration:TwoFactor')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('registration/login')
    else:
        return render(request, 'registration/login.html')

def TwoFactorAuthentication(request):
    if request.method == 'POST':

    return render(request,'registration/2FA.html')

def OTPAuthentication(request):

    return render(request,'registration/OTP_Auth.html')

def logout(request):
    auth.logout(request)
    return redirect('')
