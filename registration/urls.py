from django.conf.urls import url
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView 

urlpatterns = [
    path('login/', LoginView.as_view(template_name='registration/login.html'), name="login"),
    path('',views.registration,name="registration"),
    path('TwoFactor/',views.TwoFactorAuthentication,name="twofactor"),
    path('OTP/', views.OTPAuthentication,name="OTP_Authentication"),
    path('logout/',LogoutView.as_view(template_name='registration/logout.html'),name="logout")
]