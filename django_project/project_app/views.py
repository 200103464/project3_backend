from django.shortcuts import render,redirect,HttpResponse
from django.http import HttpResponse
from .models import *
from .forms import *
from  django.views.generic import DetailView,UpdateView,DeleteView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.core.mail import send_mail
from django.core.mail import EmailMessage

def main(request):
    return render(request,'project_app/main.html')

def send_message(request):
    send_mail('Web programming: back end', 'My contact', '200103464@stu.sdu.edu.kz',
              ['200103464@stu.sdu.edu.kz','200103231@stu.sdu.edu.kz'],
              fail_silently=False)
    return render(request, 'project_app/successfull.html')
'''
def send_message(request):
    email = EmailMessage(
        'Hello',
        'Body goes here',
        '200103464@stu.sdu.edu.kz',
        ['200103464@stu.sdu.edu.kz', '200103315@stu.sdu.edu.kz'],

        headers={'Message-ID': 'foo'},
    )
    email.attach_file(r'C:\Users\Nitro5\Downloads\Sultan Plaza Borovoe.jpg')
    email.send(fail_silently=False)
    return render(request, 'project_app/successfull.html')
'''

def register(request):
    if request.method =='POST':
        user_form=RegisterForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            username = user_form.cleaned_data.get('username')
            messages.success(request, f' Welcome to our website {username}!')
            return redirect('register')
    else:
        user_form=RegisterForm()
    return render(request,'project_app/register.html',{'user_form':user_form})
   # return render(request,'project_app/register.html')
def login(request):
    if request.method == 'POST':
        user_form = AuthenticationForm(data=request.POST)
        if user_form.is_valid():
            return redirect('home')
    else:
        user_form=AuthenticationForm()
    return render(request, 'project_app/login.html', {'user_form': user_form})
