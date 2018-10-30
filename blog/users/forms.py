from django.contrib.auth.models import User;
from django.contrib.auth.forms import UserCreationForm;
from django import forms;
class CustomRegister(UserCreationForm):
    first_name=forms.CharField(max_length=150,label="First Name");
    last_name=forms.CharField(max_length=150,label="Last Name");
    email=forms.EmailField();
    class Meta:
        model=User;
        fields=['first_name','last_name','username','email','password1','password2'];
# class
