from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User,auth
from random import randint
from django.core.mail import send_mail
from django.conf import settings
import datetime


def registration(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('../registration')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('../registration')
            else:
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                print('User created')
                return redirect('../')
        else:    
            messages.info(request,'Password not matching')
            return render(request,'registration/reg_form.html')
        # return redirect('/')
    else:
        return render(request,'registration/reg_form.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(request,username=username,password=password)
        if user is not None:
            user = User.objects.get(username=username)
            user_email = user.email
            if 'LoginBtn1' in request.POST:
                otp = randint(100000, 999999)
                print(otp)
                subject = "Login with OTP"
                email_from = settings.EMAIL_HOST_USER
                message = "This is your OTP for logging into our system : " + str(otp)
                val = send_mail(subject, message, email_from, [user_email])
                if val:
                    print('Email was sent successfully')
                    request.session['username']=username
                    request.session['password']=password
                    request.session['otp']=otp
                    return redirect('../OTP')
                else:
                    print('Email was not sent successfully')
                    return redirect('../login')
            elif 'LoginBtn2' in request.POST:
                return redirect('../QR')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('../login')
    else:
        return render(request,'registration/login.html')

def OTPAuthentication(request):
    if request.method == 'POST':
        OTP2 = request.POST['OTP']
        username = request.session['username']
        password = request.session['password']
        otp = request.session['otp']
        if (str(otp) == str(OTP2)):
            user=auth.authenticate(request,username=username,password=password)
            auth.login(request,user)
            return redirect('../../')
        else:
                print('Wrong OTP mentioned!!!')
                return redirect('../login') 
    else:
        return render(request,'registration/loginwithOTP.html')

def QRAuthentication(request):
    return render(request,'registration/loginwithQR.html')

def logout(request):
    auth.logout(request)
    return render(request,'registration/logout.html')
