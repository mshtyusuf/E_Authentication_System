from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name="login"),
    path('',views.registration,name="registration"),
    path('OTP/', views.OTPAuthentication,name="OTP_Authentication"),
    path('QR/',views.QRAuthentication,name="QR Authentication"),
    path('logout/', views.logout, name="logout")
]