from django.shortcuts import render, redirect
from .models import Food, Consume
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .decorators import *
from django.contrib.auth.models import Group
# from .filters import fooditemFilter
# Create your views here.

@login_required(login_url='login')

def index(request):

    if request.method == "POST":
        food_consumed = request.POST['food_consumed']
        consume = Food.objects.get(name=food_consumed)
        user = request.user
        consume = Consume(user=user, food_consumed=consume)
        consume.save()
        foods = Food.objects.all()

    else:
        foods = Food.objects.all()
    consumed_food = Consume.objects.filter(user=request.user)

    return render(request, 'index.html', {'foods': foods, 'consumed_food': consumed_food})

@login_required(login_url='login')

def detailfood(request,id):

   consume = Food.objects.get(id=id)
   user= request.user
   consume =Consume(user=user, food_consumed=consume)
   if request.method == 'POST':
        consume.save()
        return redirect('/')
  
   consumed_food = Consume.objects.filter(user=request.user)
   
   return render(request, 'display.html', { 'consumed_food': consumed_food})


@login_required(login_url='login')

def delete_consume(request, id):
    consumed_food = Consume.objects.get(id=id)
    if request.method == 'POST':
        consumed_food.delete()
        return redirect('/')
    return render(request, 'delete.html')

@login_required(login_url='login')

def bmi(request):
   
    return render(request,'bmi.html')  


@unauthorized_user
def registerPage(request):
    form=createUserForm()
    if request.method=='POST':
        form=createUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            username=form.cleaned_data.get('username')
            # group=Group.objects.get(name='user')
            # user.groups.add(group)
            email=form.cleaned_data.get('email')
            # Consume.objects.create(user=user)
            messages.success(request,'Account created for '+username)
            return redirect('login')
    context={'form':form}
    return render(request,'register.html',context)

@unauthorized_user
def loginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.info(request,' Invalid Credentials')
    return render(request,'login.html')

@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('login')