from django.shortcuts import render


def index(request):
    return render(request, 'main.html')


def tables(request):
    return render(request, 'tables.html')


def price(request):
    return render(request, 'price.html')


def contact(request):
    return render(request, 'contact.html')

