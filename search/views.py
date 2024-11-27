from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'search/index.html', {})

def home(request):
    return render(request, 'search/index.html', {})

def list_products(request):
    return render(request, 'search/list_products.html', {})

def contact(request):
    return render(request, 'search/contact.html', {})

def sign_in(request):
    return render(request, 'search/sign_in.html', {})

def sign_up(request):
    return render(request, 'search/sign_up.html', {})

def details(request, product_id):
    return render(request, 'search/details.html', {'product_id': product_id})
