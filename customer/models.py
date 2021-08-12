import datetime
from django.db import models

# Create your models here.
class customers(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=255, unique=True)

class product(models.Model):
    price = models.IntegerField()
    product_category = models.CharField(max_length=255)
    product_name = models.CharField(max_length=255)

class order(models.Model):
    customer_id = models.ForeignKey(customers, on_delete=models.CASCADE)
    product_id = models.CharField(product, max_length=255)
    order_date = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField()

class shipment(models.Model):
    order_id = models.ForeignKey(order, on_delete=models.CASCADE)
    shipping_mode = models.CharField(max_length=255)
    shipping_date = models.DateTimeField()
    shipping_address = models.CharField(max_length=255)



