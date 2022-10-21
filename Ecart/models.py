from email.policy import default
from django.db import models
from django.contrib.auth.models import User

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
    quantity = models.IntegerField(default = 1)