from django.shortcuts import render
from django.http import HttpResponse
from .models import *


# Create your views here.
def home(request):
    orders = Order.objects.all()  # used to show on page
    customers = Customer.objects.all()  # used to show on page
    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='pending').count()

    context = {'orders': orders, 'customers': customers, 'total_orders': total_orders, 'delivered': delivered,
               'pending': pending}

    # return HttpResponse('home')
    return render(request, 'accounts/dashboard.html', context)


def products(request):
    products = Product.objects.all()
    # return HttpResponse('products')
    return render(request, 'accounts/products.html',
                  {'products': products})  # third item: to throw out variables to template


def customers(request):
    # return HttpResponse('customer')
    return render(request, 'accounts/customer.html')
