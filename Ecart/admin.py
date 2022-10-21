from django.contrib import admin
from Ecart.models import *

class Products_view(admin. ModelAdmin):
    list_display = ['title', 'prodect_image', 'product_name', 'price', 'in_stock', 'out_of_stock']

admin.site.register(Product)