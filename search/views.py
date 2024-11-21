from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Hey ! tu es sur l'index de l'application search du projet NutriFood.</h1>")

# Create your views here.
