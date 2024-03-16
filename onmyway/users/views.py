from django.shortcuts import render, redirect
from django.contrib import messages
import re

def homepage(request):
    return render(request, 'common.html')


def register(request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        email = request.POST['email']
        phone = request.POST['phone']
        usertype = request.POST['usertype']
        govtid = request.FILES.get('govt_id', None)
        license = request.FILES.get('license', None)
        vehcilecertificate = request.FILES.get('vehiclecertificate', None)
        password = request.POST['pass']
        confpassword = request.POST['confpass']

        errors = []

        if password != confpassword:
            errors.append('Passwords do not match.')

        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            errors.append('Please enter a valid email address.')

        if not re.match(r'^[0-9]{3}-?[0-9]{3}-?[0-9]{4}$', phone):
            errors.append('Please enter a valid phone number.')

        if len(password) < 6:
            errors.append('Password should be at least 6 characters long.')

        if not any(char.isalpha() for char in password):
            errors.append('Password should contain at least one letter.')
            
        if not any(char.isdigit() for char in password):
            errors.append('Password should contain at least one digit.')

        if errors:
            for error in errors:
                messages.error(request, error)
            return redirect('register')
        
    return render(request, 'users/register.html')




def login(request):
    return render(request, 'users/login.html')


def forgotpassword(request):
    return render(request, 'users/forgotpassword.html')



def userprofile(request):
    return render(request, 'users/userprofile.html')