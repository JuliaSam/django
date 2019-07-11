from django.shortcuts import render
from .models import Product, ProductCategory

def products(request):
    context = {'products': Product.objects.all()}
    return render(request, 'mainapp/products.html', context)

def main(request):
    products = Product.objects.all()[:4]
    context = {'username': 'Юлия'}
    return render(request, 'mainapp/main.html', context)

def contacts(request):
    return render(request, 'mainapp/contacts.html')
