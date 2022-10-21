from django.shortcuts import render, redirect
from django.http import HttpResponse
#from django.views.generic import CreateView
from django.db.models import Q
from numpy import product
from Ecart.forms import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.db.models import Avg, Max, Min, Sum

def Form_in(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username =username, password = password)
        if user is not None:
            login(request,user)
            return redirect('show')
        else:
            
            form = AuthenticationForm()
            messages.info(request, 'username or password is incorrect')
            return render(request,'log_in.html',{'form':form})
    else:
        form = AuthenticationForm()
        return render(request, 'log_in.html', {'form':form})

def Form_out(request):

    logout(request)
    return redirect('login')

@login_required()
def Product_list(request):

    all = Products_details.objects.all()
    return render(request, 'show.html', {'products':all})

@login_required()
def Search(request):

    context = {}
    if 'need' in request.POST: 
  
        find = request.POST.get('need')
        all = Products_details.objects.all()
        context['product list'] = all
        suggetions_qs = Products_details.objects.filter(Q(title__icontains = find) | 
                                                         Q(name__icontains = find) |  
                                                         Q(brand__icontains = find) & 
                                                         Q(in_stock__gt = 0))
        
        context['data'] = suggetions_qs
     
    return render(request, 'search.html', context)

@login_required()
def add_to_cart(request, id, ):
    product_selected = Products_details.objects.get(id = id)
    add_cart = Carts.objects.create(user = request.user, product=product_selected)
    context = {'data': add_cart.product}
    return render(request, 'add_cart.html', context)

def Show_cart(request):

   
    total_price = Carts.objects.filter(user = request.user).aggregate(Sum('product_id__price'))
    cart_total_price = total_price['product_id__price__sum']
    cart_list = Carts.objects.filter(user = request.user)
    context = {'data':cart_list, 'total_price': cart_total_price}
    return render(request, 'cart.html', context)

def Remove_cart(request, id):

    cart_del = Carts.objects.get(id=id)
    cart_del.delete()
    return render(request, 'cart.html')









'''quantity = request.POST.get('quantity')
    carts_price = Carts.objects.filter(id = id).values()
    price = carts_price[0]['product_id__price'] * quantity
    #return render(request, 'cart.html', {'price_after_add':price})'''