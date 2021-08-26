import datetime
from django.db import models


# Create your models here.
class customer(models.Model):
    name = models.CharField(max_length=255, null = True)
    address = models.CharField(max_length=255, null = True)
    phone = models.CharField(max_length=12, null = True)
    email = models.CharField(max_length=255, unique=True)

def __str__(self):
    return self.name

class product(models.Model):
    price = models.IntegerField()
    product_category = models.CharField(max_length=255)
    product_name = models.CharField(max_length=255, default="NN")
   
def __str__(self):
    return self.product_name

class order(models.Model):
    customer_id = models.ForeignKey(customer, on_delete=models.CASCADE, null = True, blank = True)
    product_id = models.ForeignKey(product, on_delete=models.CASCADE, null = True, blank = True)
    order_date = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=0)

def __str__(self):
    return self.product_id.product_name

class shipment(models.Model):
    order_id = models.ForeignKey(order, on_delete=models.CASCADE)
    shipping_mode = models.CharField(max_length=255)
    shipping_date = models.DateTimeField(auto_now_add=True)
    shipping_address = models.CharField(max_length=255)

def __str__(self):
    return self.order_id
