from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.

def home(request):
    return render(request, "mysite/home.html")

#Cat view

def allProdCat(request,c_slug=None):
    c_page = None
    product = None
    if c_page!=None:
        c_page = get_object_or_404(Category,slug=c_slug)
        products = Product.objects.filter(category=c_page,available=True)
    else:
        products = Product.objects.all().filter(available=True)
    return render(request,'mysite/category.html', {'category': c_page, 'products': products})
