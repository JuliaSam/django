from django.shortcuts import render

def products(request):
    return render(request, 'mainapp/products.html')

def main(request):
    context = {'username': 'Юлия', 'array': ['Платья', 'Украшения', 'Цветы', 'Услуги']}
    return render(request, 'mainapp/main.html', context)

def contacts(request):
    return render(request, 'mainapp/contacts.html')
