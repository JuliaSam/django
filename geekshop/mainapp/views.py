from django.shortcuts import render

def products(request):
    return render(request, 'mainapp/products.html')

def main(request):
    return render(request, 'mainapp/main.html')

def contacts(request):
    return render(request, 'mainapp/contacts.html')
