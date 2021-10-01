from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from core.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from listing.models import Listing
from django.contrib.auth.hashers import check_password

import random
import string

# Create your views here.
def Confirmation_code(code_length= 6):
    code= string.hexdigits
    return ''.join(random.choice(code) for i in range(code_length))

confirm_code = Confirmation_code()

def register(request):
    if request.method == 'POST':
        first_name= request.POST['first_name']
        last_name= request.POST['last_name']
        username= request.POST['username']
        email= request.POST['email']
        phone= request.POST['phone']
        password= request.POST['password']
        password1= request.POST['password1']
        user= User

        context= {
            'first_name': first_name,
            'last_name': last_name,
            'username': username,
            'email': email,
            'phone': phone,
            'password': password,
            'password1': password1,
        }
        if password == password1:
            if user.objects.filter(email= email).exists():
                messages.error(request, 'This Email is already Exists')
                return redirect('register')
            else:
                if user.objects.filter(username= username).exists():
                    messages.error(request, 'The Username is already Exists')
                    return redirect('register')
                else:
                    if user.objects.filter(phone= phone).exists():
                        messages.error(request, 'The Phone Number is already Exists')
                        return redirect('register')
                    else:
                        send_mail(
                            subject= 'Account Creation Confirmation',
                            message= 'Hi '+ first_name + ' You Confirmation code is: ' +confirm_code,
                            from_email= settings.EMAIL_HOST_USER,
                            recipient_list= [email],
                            fail_silently= False
                        )
                        return render(request, 'accounts/confirmregister.html', context= context)

        else:
            messages.error(request, 'The Two Passwords Do Not Match')
            return redirect('register')

    else:
        return render(request, 'accounts/register.html', context= None)



def confirmregister(request):
    if request.method == 'POST':
        first_name= request.POST['first_name']
        last_name= request.POST['last_name']
        username= request.POST['username']
        email= request.POST['email']
        phone= request.POST['phone']
        password= request.POST['password']
        confirm_code = request.POST['code']
        user= User

        context= {
            'first_name': first_name,
            'last_name': last_name,
            'username': username,
            'email': email,
            'phone': phone,
            'password': password,
        }

        if confirm_code == confirm_code:
            user= user.objects.create_user(email= email, username= username, first_name= first_name, last_name= last_name, phone= phone, password= password)
            user.save()
            login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('index')

        else:
            messages.error(request, 'Invalid Confirmation Code')
            return render(request, 'accounts/confirmregister.html', context= context)

    else:
        return redirect('confirm_register')


def userlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password= request.POST['password']
        user= authenticate(username= username, password= password)

        if user is not None:
            login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('index')

        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')

    else:
        return render(request, 'accounts/login.html', context= None)


@login_required
def userlogout(request):
    logout(request)
    return HttpResponseRedirect('/')


def userdashboard(request):
    listings= Listing.objects.order_by('-list_date').filter(owner= request.user)
    context= {
        'listings': listings,    
    }
    return render(request, 'accounts/dashboard.html', context= context)


def change_password(request):
    if request.method=='POST':
        user= request.user
        currentpassword= request.POST['currentpassword']
        
        if not check_password(currentpassword, user.password):
            messages.error(request, 'Incorrect Current Password')
            return redirect('index')
        
        password1= request.POST['password1']
        password2= request.POST['password2']
        
        if password1 == password2:
            user.set_password(password1)
            user.save()
            messages.success(request,'You have successfully changed the password')
            
        else:
            messages.error(request,'Passwords do not match')
        return redirect('index')
        
    else:
        return render(request,'accounts/change_password.html')