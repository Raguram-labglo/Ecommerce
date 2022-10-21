from django.db import models

class Product(models.Model):
    title = models.CharField(max_length= 100)
    image = models.ImageField(upload_to = "prodects_img/", null=True)
    name = models.CharField(max_length = 50)
    brand = models.CharField(max_length = 40)
    price = models.IntegerField()
    in_stock = models.IntegerField()
    quantity = models.IntegerField()


'''class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete = )
'''