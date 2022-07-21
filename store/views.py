from django.shortcuts import render
# from django.http import HttpResponse
from .models import Customer


def responder(request):
    query = Customer.objects.filter(gender__contains='M')

    
    return render(request, 'index.html', {'name':query})
