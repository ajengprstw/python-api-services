from django.contrib import admin
from .models import customers, product, order, shipment

# Register your models here.
admin.site.register(customers)
admin.site.register(product)
admin.site.register(order)
admin.site.register(shipment)
