from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User,auth
from random import randint
from django.core.mail import send_mail,EmailMessage
from django.conf import settings
from django.views.decorators.cache import cache_control
import qrcode,pyzbar

location = "F:/NIIT University/4 Year/Capstone Project 2/Project/"
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
                sender = settings.EMAIL_HOST_USER
                message = "Hi,"+ str(user.first_name)+", this is your OTP for logging into our system : " + str(otp) + ". Please login within 5 minutes."
                val = send_mail(subject, message, sender, [user_email])
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
                qr = qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=5,border=5)
                qr.add_data(username + ' ' + password)
                qr.make(fit=True)
                img = qr.make_image(fill_color='black', back_color='white')
                img.save(location+'qrcode_'+str(user.username) +'.png')
                print('QR Code generated!!')
                
                email_sender = settings.EMAIL_HOST_USER
                subject = "Login with QR"
                message = "Hi,"+ str(user.first_name)+", the QR for logging into our system is attached. Please login within 5 minutes."
                mail = EmailMessage(subject,message,email_sender,[user_email])
                mail.attach_file(location+'qrcode_'+str(username)+'.png')
                val = mail.send()
                if val:
                    print('Email was sent successfully')
                    request.session['username']=username
                    request.session['password']=password
                    return redirect('../QR')
                else:
                    print('Email was not sent successfully')
                    return redirect('../login')
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
    if request.method == 'POST':
        #Take the session variable
        username = request.session['username']
        password = request.session['password']

        #Take the variables from QR Code reader template
        credentials = request.POST['b']
        temp = credentials.split(" ")
        username2 = temp[0]
        password2 = temp[1]
        if (str(username)== str(username2) and str(password) ==str(password2)):
            user=auth.authenticate(request,username=username,password=password)
            auth.login(request,user)
            return redirect('../../')
        else:
           print('Invalid credentials!!!')
        return redirect('../login')
    else:
        return render(request,'registration/loginwithQR.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def logout(request):
    auth.logout(request)
    request.session.flush()
    return redirect('../../')