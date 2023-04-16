from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'homepage.html')

def cadastro(request):
    return render(request, 'cadastro.html')

def vinhos(request):
    return render(request, 'vinhos.html')
