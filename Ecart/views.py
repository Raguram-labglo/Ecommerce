from django.shortcuts import render, redirect
from django.db.models import Q
from Ecart.forms import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.db.models import Sum

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

@login_required
def Product_list(request):

    all_product = Products_details.objects.all()
    wish = Wish_list.objects.get(user = request.user)
    wish_product = wish.favourite.all()
    alredy_wish = list(wish_product)
    return render(request, 'show.html', {'products':all_product, 'wish':wish_product, 'alredy':alredy_wish})

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
    product_selected = Products_details.objects.get(id = id)
    price_of_product = product_selected.price
    add_cart = Carts.objects.create(user = request.user, product=product_selected , price = price_of_product)
    context['data'] = add_cart.product
    context['pricedata'] = add_cart
    return render(request, 'add_cart.html', context)

@login_required()
def Show_cart(request):

    cart_list = Carts.objects.filter(Q(user = request.user) & Q(is_active = True))
    total_price = cart_list.aggregate(Sum('price'))
    cart_total_price = total_price['price__sum']
    context = {'data':cart_list, 'total_price': cart_total_price}
    return render(request, 'cart.html', context)

def Update_cart(request,id):
    quantity = request.POST.get('quantity')
    update_cart = Carts.objects.get(id = id)
    update_cart.quantity = quantity
    update_cart.price = update_cart.product.price * int(quantity)
    update_cart.save()
    return render(request, 'cart.html')
@login_required()
def Remove_cart(request, id):

    cart_del = Carts.objects.get(id=id)
    cart_del.delete()
    return render(request, 'cart.html')

@login_required()
def Order_details(request):
    
    get_order = Order.objects.get(user = request.user)
    total_orders_price = Order.objects.filter(user = request.user).aggregate(Sum('order_items__price'))
    price = total_orders_price['order_items__price__sum']
    if price == None:
        context = {'message': 'your order page is empty'}
        return render(request, 'order_details.html', context)
    tax = int(18/100*price)
    tax_price = price +tax
    order_product = get_order.order_items.all()
    context = {'order_product':get_order, 'data' : order_product, 'price':price, 'tax':tax, 'tax_price':tax_price}
    return render(request, 'order_details.html', context)

@login_required
def Create_order(request):
    orders = Order.objects.get_or_create(user = request.user)
    order_update = Order.objects.get(user = request.user)
    order_update.order_items.add(*Carts.objects.filter(user = request.user))
    inactive  = Carts.objects.filter(user = request.user)
    inactive.update(is_active = False)
    order_update.save()
    return redirect('cart')

@login_required()
def Cancel_order(request, id):
    product = Carts.objects.get(id = id)
    product.delete()
    return render(request, 'order_details.html') 

@login_required
def Wish_list_products(request, id):

    wish_product = Products_details.objects.get(id = id)
    
    obj,add_wish = Wish_list.objects.get_or_create(user = request.user)
    add_fav = Wish_list.objects.get(user = request.user)
    add_fav.favourite.add(Products_details.objects.get(id = id))
    return render (request, 'wish_page.html', {'wish': wish_product})

@login_required()
def Show_wish(request):

    wished_products = Wish_list.objects.get(user = request.user)
    context = {'wish_list':wished_products.favourite.all()}
    return render(request, 'wish_list.html', context)