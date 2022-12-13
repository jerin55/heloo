from atexit import register
from multiprocessing import context
from time import timezone
from django.shortcuts import render,redirect

from django.contrib.auth.decorators import login_required

from django.contrib.auth import login

import datetime
from django.contrib.auth.models import User,auth
from django.contrib import messages

from app1.models import Category, Order, OrderItem, Product
from django import template


# Create your views here.



def home(request):
    product=Product.objects.all()
    context={'product':product}
    return render(request,'homepage.html',context)

@login_required(login_url='uslogin')
def Adminhome(request):
    if not request.user.is_staff:
        return redirect('home')
    product=Product.objects.all()
    context={'product':product}
    return render(request,'adhom.html',context)    

   


def uslogin(request):
    return render(request,'login.html')  

def loginuser(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user =auth.authenticate(username=username,password=password)
        request.session["uid"] = user.id      
        if user is not None:
            if user.is_staff:
                login(request,user)
                return redirect('Adminhome')
            else:
                auth.login(request,user)
                messages.info(request, 'welcome' )
                return redirect('home')
        else:
            messages.info(request,'invalid username or password')
            return redirect('login')   

    else:
        return redirect('login') 


def logout(request):
    request.session["uid"] = ""
    auth.logout(request)
    return redirect('home')       


def signup(request):
    if request.method=='POST':
        first_name=request.POST['first_name'] 
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['cpassword']  

        usr=User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=password,
            cpassword=cpassword
        )    

        usr.save()
        print('success')
        return redirect('/')
    else:
        return render(request,'signup.html')      


def userceate(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['cpassword']


        if password==cpassword:
            if User.objects.filter(username=username).exists():

                messages.info(request,'username already exists')
                return redirect('signup')

            else:
                urs=User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    email=email,
                    password=password,
                ) 
                urs.save()

                

        else:
            messages.info(request,'password incorrect')    
            return redirect('signup') 
        return redirect('signup')    
    else:
        return render(request,'signup.html')    

@login_required(login_url='uslogin')
def addproduct(request):
    if not request.user.is_staff:
        return redirect('uslogin')
    cat=Category.objects.all()
    context={'catg':cat}
    return render(request,'addproduct.html',context)

def addpr(request):
    if request.method=='POST':
        name=request.POST['name']
        price=request.POST['price']
        count=request.POST['count']
        sel=request.POST['sel']
        category1=Category.objects.get(id=sel)
        user_image=request.FILES.get('user_image')

        prdct=Product(
            name=name,
            price=price,
            count=count,
            user_image=user_image,
            category=category1

        )
        prdct.save()
        return redirect('Adminhome')

@login_required(login_url='uslogin')
def prodes(request,pk):
    prod=Product.objects.get(id=pk)
    return render (request,'des.html',{'product':prod})




def addcart(request,pk):
    product=Product.objects.get(id=pk)   

    order_item, created =OrderItem.objects.get_or_create(
        product=product,
        user=request.user,
        ordered=False,

    )
    order_qs=Order.objects.filter(user=request.user,ordered=False)
    if order_qs.exists():
        order=order_qs[0]
        if order.items.filter(product__pk=pk).exists():
            order_item.quantity +=1
            order_item.save()
            messages.info(request,"Added successfully")
            return redirect('prodes',pk=pk)
        else:
            order.items.add(order_item)
            messages.info(request,"Added successfully")
            return redirect('prodes',pk=pk)
    else:
       
          
        messages.info(request,'Added Successfully') 
        return redirect('prodes',pk=pk)  


def nw(request):
    return render(request,'nw.html')   

@login_required(login_url='uslogin')
def orderlist(request):
    order=OrderItem.objects.filter(user=request.user)
    return render(request,'orderlist.html',{'order':order})
          

def admincart(request):
    if not request.user.is_staff:
        return redirect('home')
    ord=OrderItem.objects.all()
    return render(request,'admorder.html',{'ord':ord})

@login_required(login_url='uslogin')    
def users(request):
    if not request.user.is_staff:
        return redirect('home')
    users=User.objects.all()
    return render(request,'userstable.html',{'users':users})

@login_required(login_url='uslogin')
def deluser(request,pk):
    if not request.user.is_staff:
        return redirect('home')
    delete=User.objects.get(id=pk)
    return render(request,'deleteuser.html',{'delst' :delete})    

def deleteuser(request,pk):
    delist=User.objects.get(id=pk)
    delist.delete()
    return redirect('Adminhome')
       

   

@login_required(login_url='uslogin')
def er(request):
    return render(request,'user.html')                    