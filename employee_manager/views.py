from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'employee_manager/home.html')

def about(request):
    return render(request,'employee_manager/about.html')

def contact(request):
    return render(request,'employee_manager/contact.html')