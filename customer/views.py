from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

from .models import *
from .forms import OrderForm

#create your views here

def index(request):
    Orders = order.objects.all()
    Customers = customer.objects.all()
    total_customers = Customers.count()

    context = {'orders': Orders,
               'customers': Customers,
               'total_customers': total_customers}
    

    return(render(request, 'customer/dashboard.html', context))

def Product(request):
	Product = product.objects.all()

	return render(request, 'customer/products.html', {'product':Product})

def Customer(request, pk_test):
	Customer = customer.objects.get(id=pk_test)

	Orders = Customer.order_set.all()
	Order_count = Orders.count()

	context = {'customer':Customer, 'orders':Orders, 'order_count':Order_count}
	return render(request, 'customer/customer.html',context)

def createOrder(request):
	form = OrderForm()
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = OrderForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'customer/order_form.html', context)

def updateOrder(request, pk):

	Order = order.objects.get(id=pk)
	form = OrderForm(instance=Order)

	if request.method == 'POST':
		form = OrderForm(request.POST, instance=Order)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'customer/order_form.html', context)

def deleteOrder(request, pk):
	Order = order.objects.get(id=pk)
	if request.method == "POST":
		Order.delete()
		return redirect('/')

	context = {'item':Order}
	return render(request, 'customerdelete.html', context)