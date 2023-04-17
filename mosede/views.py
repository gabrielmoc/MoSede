from django.http import HttpResponse
from django.shortcuts import render
from mosede.models import Wine, Cerveja, Whisky, Enlatado, Vodka, Drink

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

def enlatados(request):
    enlatados = Enlatado.objects.all()
    return render(request, 'enlatados.html', {"cards": enlatados})

def vodkas(request):
    vodkas = Vodka.objects.all()
    return render(request, 'vodkas.html', {"cards": vodkas})

def drinks(request):
    drinks = Drink.objects.all()
    return render(request, 'drinks.html', {"cards": drinks})

