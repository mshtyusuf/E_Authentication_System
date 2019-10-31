from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    First_Name = models.CharField(max_length=30,default='')
    Last_Name = models.CharField(max_length=30,default='')
    Email = models.EmailField()
    Phone = models.CharField(max_length=12)

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)