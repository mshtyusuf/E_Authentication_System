from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User,auth
from random import randint
from django.core.mail import send_mail
from django.conf import settings
# from django.contrib.auth.decorators import login_required

otp = 0
active_user = {}
def registration(request):
    if request.method=='POST':
        first_name=request.POST.get['first_name']
        last_name=request.POST.get['last_name']
        username=request.POST.get['username']
        password1=request.POST.get['password1']
        password2=request.POST.get['password2']
        email=request.POST.get['email']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return render(request,'registration/reg_form.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return render(request,'registration/reg_form.html')
            else:
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                print('User created')
                return redirect('/')
        else:    
            messages.info(request,'Password not matching')
            return render(request,'registration/reg_form.html')
        # return redirect('/')
    else:
        return render(request,'registration/reg_form.html')

def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=auth.authenticate(request,username=username,password=password)
        if user is not None:
            user = User.objects.get(username=username)
            user_email = user.email
            print(user_email)
            if 'LoginBtn1' in request.POST:
                otp = randint(100000, 999999)
                subject = "Login with OTP"
                email_from = settings.EMAIL_HOST_USER
                message = "This is your OTP for logging into our system : " + str(otp)
                val = send_mail(subject, message, email_from, [user_email])
                if val:
                    print('Email was sent successfully')
                    request.session['username']=username
                    request.session['password']=password
                    return render(request,'registration/loginwithOTP.html')
                else:
                    print('Email was not sent successfully')
                    return redirect('')
            elif 'LoginBtn2' in request.POST:
                return render(request,'registration/loginwithQR.html')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('')
    else:
        return render(request,'registration/login.html')

def OTPAuthentication(request):
    if request.method == 'POST':
        OTP2 = request.POST['OTP']
        print(OTP2)
        if (otp == OTP2):
            username = request.session['username']
            password = request.session['password']
            print(username)
            print(password)
            auth.login(username,password)
            return redirect('')
        else:
            print('Wrong OTP mentioned!!!')
            return redirect('registration/login')
    else:
        return render(request,'registration/OTP_Auth.html')

def logout(request):
    auth.logout(request)
    return render(request,'registration/logout.html')
