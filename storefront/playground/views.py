from ast import Or
from django.shortcuts import render
from django.http import HttpResponse
from store.models import OrderItem,Product,Collection

def say_hello(request):
    query_set = OrderItem.objects.filter(product__collection__id=3)
    return render (request, 'hello.html', {'name':'Suren' , 'products' : query_set})