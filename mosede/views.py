from django.http import HttpResponse
from django.shortcuts import render
from mosede.models import Wine, Cerveja, Whisky

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'homepage.html')

def cadastro(request):
    return render(request, 'cadastro.html')

def vinhos(request):
    vinhos = Wine.objects.all()
    return render(request, 'vinhos.html', {"cards": vinhos})

def cervejas(request):
    cervejas = Cerveja.objects.all()
    return render(request, 'cervejas.html', {"cards": cervejas})

def whiskys(request):
    whiskys = Whisky.objects.all()
    return render(request, 'whiskys.html', {"cards": whiskys})

