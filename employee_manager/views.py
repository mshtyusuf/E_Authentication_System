from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request,'employee_manager/home.html')

@login_required
def about(request):
    return render(request,'employee_manager/about.html')

@login_required
def contact(request):
    return render(request,'employee_manager/contact.html')