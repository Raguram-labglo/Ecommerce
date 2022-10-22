from django.shortcuts import render, redirect
from django.db.models import Q
from Ecart.forms import *
from django.contrib.auth import authenticate,login,logout
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
        suggetions_qs = Products_details.objects.filter(Q(title__icontains = find) | Q(name__icontains = find) | Q(brand__icontains = find) & Q(in_stock__gt = 0))        
        context['data'] = suggetions_qs
    return render(request, 'search.html', context)

@login_required()
def add_to_cart(request, id):
    context = {}
    if 'quantity' in request.POST:
        product_selected = Products_details.objects.get(id = id)
        quantity_product = request.POST.get('quantity')
        price_of_product = product_selected.price * int(quantity_product)
        add_cart = Carts.objects.create(user = request.user, product=product_selected , price = price_of_product ,quantity= quantity_product)
        context['data'] = add_cart.product
        context['pricedata'] = add_cart
        print(context)  
    return render(request, 'add_cart.html', context)

@login_required()
def Show_cart(request):
    quantity_product = request.POST.get('quantity')
    total_price = Carts.objects.filter(user = request.user).aggregate(Sum('price'))
    cart_total_price = total_price['price__sum']
    cart_list = Carts.objects.filter(user = request.user)
    context = {'data':cart_list, 'total_price': cart_total_price}
    return render(request, 'cart.html', context)

@login_required()
def Remove_cart(request, id):

    cart_del = Carts.objects.get(id=id)
    cart_del.delete()
    return render(request, 'cart.html')

@login_required()
def Order_plasement(request, id):
    order_product = Carts.objects.get(id = id)
    orders = Order.objects.create(user = request.user, order_items = order_product)
    context = {'data':orders.order_items}
    return render(request, 'order_page.html', context)