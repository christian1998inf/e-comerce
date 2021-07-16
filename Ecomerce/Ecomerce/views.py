from django.http import HttpResponse, request
import datetime
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render

def plantilla(request): 

    return render(request,"index.html")

def cart(request):
    return render(request, "cart.html")

def checkout(request):
    return render(request,"checkout.html")

def product(request):
    return render(request, "product.html")

def contact(request):
    return render(request, "contact.html") #Para ingresar la plantilla a la url Django 