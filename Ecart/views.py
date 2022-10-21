from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import CreateView
from django.db.models import Q
from Ecart.forms import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages


'''def Add_product(request):

    form = Prodect_form (request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()  
    return render(request, 'add_prod.html', {'data':form})'''

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
    all = Product.objects.all()
    return render(request, 'show.html', {'products':all})
@login_required()
def Search(request):
    context = {}
    if 'need' in request.POST:        
        find = request.POST.get('need')
        all = Product.objects.all()
        context['product list'] = all
        suggetions_qs = Product.objects.filter(Q(title__icontains = find) | Q(name__icontains = find) | Q(brand__icontains = find) & Q(in_stock__gt = 0))
        context['data'] = suggetions_qs
    return render(request, 'search.html', context)

'''@login_required()
def add_to_cart(request, id):
'''