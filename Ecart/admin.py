from django.contrib import admin
from Ecart.models import *


admin.site.register(Products_details)

class Cart_list(admin.ModelAdmin):
    list_display = ('id','user', 'product', 'price', 'quantity')
admin.site.register(Carts, Cart_list)

class Order_list(admin.ModelAdmin):
    list_display = ('id','user', 'order_status')
admin.site.register(Order, Order_list)