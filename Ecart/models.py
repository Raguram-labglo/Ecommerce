from email.policy import default
from random import choices
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
    user = models.CharField(max_length = 50, null = True)
    product = models.ForeignKey(Products_details,  null = True, on_delete = models.CASCADE)
    price = models.IntegerField(null = True)
    quantity = models.IntegerField(default = 1)

class Order(models.Model):
    user = models.CharField(max_length = 100)
    order_items = models.ManyToManyField(Carts)
    order_status = models.CharField(max_length = 60, choices = order, default = 'pending')