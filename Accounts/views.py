from django.shortcuts import render
from django.http import HttpResponse

from .models import *
# Create your views here.

def home(request):
	orders=Order.objects.all()
	customer=Customer.objects.all()

	total_customer=customer.count()
	total_order=orders.count()
	delivered=orders.filter(status='Delivered').count()
	pending=orders.filter(status='Pending').count()

	context={'orders':orders,'customer':customer,'total_order':total_order,'delivered':delivered,'pending':pending}
	return render(request, 'accounts/dashboard.html',context)

def products(request):
	products=Product.objects.all()
	return render(request, 'accounts/products.html',{'products':products})

def customer(request,pk_test):
	customer=Customer.objects.get(id=pk_test)
	orders=customer.order_set.all()
	order_count=orders.count()

	context={'customer':customer,'orders':orders,'order_count':order_count}

	return render(request, 'accounts/customer.html',context)

def status(request):
	return render(request,'accounts/status.html')
	
def contacts(request):
	return render(request,'accounts/contacts.html')
