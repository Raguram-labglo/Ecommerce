from django.db import models
from django.contrib.auth.models import User
order = [('pending', 'pending'), ('shipping', 'shipping'), ('delivered', 'delivered')]
class Products_details(models.Model):
    title = models.CharField(max_length= 100)
    image = models.ImageField(upload_to = "prodects_img/", null=True)
    name = models.CharField(max_length = 50)
    brand = models.CharField(max_length = 40)
    price = models.IntegerField()
    in_stock = models.IntegerField()
    
    
class Carts(models.Model):
    user = models.CharField(max_length = 50)
    product = models.ForeignKey(Products_details,  null = True, on_delete = models.CASCADE)
    price = models.IntegerField(null = True)
    quantity = models.IntegerField(default = 1)
    is_active = models.BooleanField(default = True)

class Order(models.Model):
    user = models.CharField(max_length = 100)
    order_items = models.ManyToManyField(Carts)
    order_status = models.CharField(max_length = 60, choices = order, default = 'pending')

class Wish_list(models.Model):
    user = models.CharField(max_length = 100)
    favourite = models.ManyToManyField(Products_details)
    wished = models.BooleanField(default = True)
