from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect,HttpResponse
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
from .filters import fooditemFilter
import requests
# Create your views here.

@login_required(login_url='login')

def index(request):
    try:
       obj1=Profile.objects.get(user=request.user)
    except:
       obj1=Profile.objects.create(user=request.user)
    food =Food.objects.filter()
    myfilter = fooditemFilter(request.GET,queryset=food)
    

    if request.method == "POST":
        food_consumed = request.POST['food_consumed']
        consume = Food.objects.get(name=food_consumed)
        user = request.user
        consume = Consume(user=user, food_consumed=consume)
        consume.save()
        foods = myfilter.qs
        
    else:
        foods =myfilter.qs
    consumed_food = Consume.objects.filter(user=request.user)

    return render(request, 'index.html', {'foods': foods, 'consumed_food': consumed_food,'myfilter':myfilter, 'profile':obj1,})

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

def reset(request):
    consumed_food = Consume.objects.filter(user=request.user)
    if request.method == 'POST':
        consumed_food.delete()
        return redirect('/')
    return render(request, 'reset.html')

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


@login_required(login_url='login')
# @allowed_users(allowed_roles=['admin'])
def fooditem(request):
    breakfast=Category.objects.filter(name='breakfast')[0].food_set.all()
    bcnt=breakfast.count()
    lunch=Category.objects.filter(name='lunch')[0].food_set.all()
    lcnt=lunch.count()
    dinner=Category.objects.filter(name='dinner')[0].food_set.all()
    dcnt=dinner.count()
    snacks=Category.objects.filter(name='snacks')[0].food_set.all()
    scnt=snacks.count()
    context={'breakfast':breakfast,
              'bcnt':bcnt,
              'lcnt':lcnt,
              'scnt':scnt,
              'dcnt':dcnt,
              'lunch':lunch,
              'dinner':dinner,
              'snacks':snacks,
            }
    return render(request,'fooditem.html',context)

@login_required(login_url='login')
# @allowed_users(allowed_roles=['admin'])
# @unauthorized_user

def createfooditem(request):
    api_url = 'https://api.calorieninjas.com/v1/nutrition?query='
    query = ''
    searchquery=request.GET.get('searchquery')
    print (searchquery)
    if searchquery is not None:
      query = searchquery
    response = requests.get(api_url + query, headers={'X-Api-Key': 'oUqvROZU7DmOYcEgLLLxFA==Oyih5zrrT6A2vFp7'})
    data=response.json()
    # print(data)
    # if response.status_code == requests.codes.ok:
    #    print(response.text)
    # else:
    #     print("Error:", response.status_code, response.text)
    items=data['items']
    
    form = fooditemForm()
    if request.method == 'POST':
        form = fooditemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form,'items':items}
    return render(request,'createfooditem.html',context)  


@login_required(login_url='login')

def editprofile(request,id):
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(User, id=id)
    form = ProfileUpdateForm(request.POST or None, instance = obj)
 
    # pass the object as instance in form
    try:
       obj1=Profile.objects.get(user=request.user)
       form1 = ProfileUpdateForm2(request.POST or None, instance = obj1)
    except:
       obj1=Profile.objects.create(user=request.user)
       form1 = ProfileUpdateForm2(request.POST or None, instance = obj1)    
    
    if form.is_valid() and form1.is_valid():
        form.save()
        form1.save()
        return HttpResponseRedirect("/profile/update/"+id)
 
    # add form dictionary to context
    context={'form':form, 'form1':form1}
    # context1["form1"] = form1
    return render(request, "editprofile.html", context)   


from locale import currency
from django.shortcuts import render
from MyFitnessFriend.settings import RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY
import razorpay
# Create your views here.
client = razorpay.Client(auth=(RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY))
def pay(request):
   # DATA = {
   # "amount": 100,
    #"currency": "INR",
    #"receipt": "receipt#1",
    #"notes": {
       # "key1": "value3",
        #"key2": "value2"
    #}
    #}
    amountdonated=request.GET.get('amountdonated')
    order_amount=500
    if amountdonated is not None:
        order_amount=int(amountdonated)
    order_amountp=order_amount*100
    order_currency='INR'
    payment_order=client.order.create(dict(amount=order_amountp,currency=order_currency,payment_capture=1))
    payment_order_id=payment_order['id']
    context ={
        'amount': order_amount, 'api_key':RAZORPAY_API_KEY ,'order_id':payment_order_id
    }
    return render(request,'pay.html',context)