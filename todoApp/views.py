from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request,'todoApp/home.html',{})

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # check password
        if len(password) < 6:
            messages.error(request,'Password must be at least 6 characters')
            return redirect('register')

        get_all_users_by_username = User.objects.filter(username=username)
        if get_all_users_by_username:
            messages.error(request,'error, username already exits, User another !')
            return redirect('register')

        new_user = User.objects.create_user(username=username,email=email,password=password)
        new_user.save()
        messages.success(request,'User succesfully created, login now ')
        return redirect('login')
    return render(request,'todoApp/register.html',{})

def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')

        validates_user = authenticate(username=username,password=password)
        if validates_user is not None:
            login(request,validates_user)
            return redirect('home-page')
        else:
            messages.error(request,'Error, wrong user details or does not exits!')
            return redirect('login')

    return render(request,'todoApp/login.html',{})

