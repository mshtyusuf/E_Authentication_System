from django.shortcuts import render,HttpResponse

# Create your views here.
def registration(request):
    return render(request,'registration/reg_form.html')

def home(request):
    return render(request,'registration/home.html')
