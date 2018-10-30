from django.shortcuts import render,redirect;
from django.contrib.auth.forms import UserCreationForm;
from django.contrib.auth.models import User;
from django.contrib import messages;
# Create your views here.
from users.forms import CustomRegister;
from django.contrib.auth.decorators import login_required;
def register(request):
    form = CustomRegister();
    if request.method=='POST':
        form=CustomRegister(request.POST);
        if form.is_valid():
            username=form.cleaned_data.get('username');
            form.save();
            messages.success(request,f'user {username} created successfully');
            return redirect('blog_home');#blog_home
    else:
        form=CustomRegister();
    return render(request,"registeration/register.html",{"form":form});
@login_required
def profile(request):
    return render(request,'registeration/profile.html')
