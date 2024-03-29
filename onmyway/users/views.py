
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
import re
from .models import CustomUser, UserFiles


def homepage(request):
    return render(request, 'common.html')


def register(request):
    errors = []
    if request.method == 'POST':
        fullname = request.POST['fullname']
        email = request.POST['email']
        phone = '+91' + request.POST['phone']
        usertype = request.POST['usertype']
        govtid = request.FILES.get('govt_id', None)
        license = request.FILES.get('license', None)
        vehiclecertificate = request.FILES.get('vehiclecertificate', None)
        password = request.POST['pass']
        confpassword = request.POST['confpass']

        if password != confpassword:
            errors.append('Passwords do not match.')

        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            errors.append('Please enter a valid email address.')

        if not re.match(r'^\+91[6-9][0-9]{9}$', phone):
            errors.append('Please enter a valid phone number.')

        if len(password) < 6:
            errors.append('Password should be at least 6 characters long.')

        if not any(char.isalpha() for char in password):
            errors.append('Password should contain at least one letter.')

        if not any(char.isdigit() for char in password):
            errors.append('Password should contain at least one digit.')

        if CustomUser.objects.filter(email=email).exists():
            errors.append('Email already exists')

        if CustomUser.objects.filter(phone=phone).exists():
            errors.append('Phone already exists')

        if errors:
            for error in errors:
                messages.error(request, error)
            return redirect('register')
        else:
            hashed_password = make_password(password)
            user = CustomUser.objects.create(
                email = email,
                fullname = fullname,
                phone = phone, 
                password = hashed_password,
                usertype = usertype
            )
            user.save()
            print('saved')
            
            userfiles = UserFiles.objects.create(
                userfile = user,
                govtid = govtid,
                license = license,
                vehiclecertificate = vehiclecertificate
            )
            userfiles.save()      
            return redirect('user_login')
    return render(request, 'users/register.html')


def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('userprofile')
        else:
            messages.error(request, "Invalid email or password. Please try again")
            return redirect('user_login')
    return render(request, 'users/login.html')


def user_logout(request):
    messages.success(request, "Logout successful")
    logout(request)
    return redirect('user_login')


def forgotpassword(request):
    return render(request, 'users/forgotpassword.html')


def userprofile(request):
    return render(request, 'users/userprofile.html')