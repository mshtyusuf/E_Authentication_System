from django.shortcuts import render,redirect
from django.urls import reverse
from registration.forms import RegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

# Create your views here.
def registration(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('employee_manager/home.html'))
    else:
        form = RegistrationForm()   
    args = {'form': form}
    return render(request, 'employee_manager/home.html', args)

def login(request):
    return render(request,'registration/login.html')
