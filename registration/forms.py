from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from registration.models import UserProfile

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.CharField(required=True,max_length=12)

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'phone',
            'password1',
            'password2'
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        
        #Sanitizing the inputs from CSRFs
        user.username = self.cleaned_data['username']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.phone = self.cleaned_data['phone']

        if commit:
            user.save()
        return user



'''
Not Logged In - Home | About Us | Contact | Login/Register
When logged in - Dashboard | Logout | Employee detail 
'''