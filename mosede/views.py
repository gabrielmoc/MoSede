from mosede.models import Wine, Cerveja, Whisky, Enlatado, Vodka, Drink
from mosede.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from mosede.backends import EmailBackend
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from mosede.forms import EmailAuthenticationForm
# def index(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         user = authenticate(request, email=email, password=password)
#         print(user, password, email)
#         if user is not None and user.is_active:
#             login(request, user)
#             print(teste)
#             print(user.is_authenticated)
#             return redirect('homepage')
#         else:
#             error_message = "Email ou senha inválidos"
#             return render(request, 'index.html', {'error_message': error_message})
#     else:
#         return render(request, 'index.html')
class index(LoginView):
    authentication_form = EmailAuthenticationForm
    template_name = 'index.html'

def homepage(request):
    return render(request, 'homepage.html')

def cadastro(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        name = request.POST.get('name')
        age = request.POST.get('age')
        user = User(email=email, password=password, name=name, age=age)
        user.save()
        return redirect('homepage')
    else:
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

def topsellers(request):
    drinks = Drink.objects.all()
    vodkas = Vodka.objects.all()
    enlatados = Enlatado.objects.all()
    whiskys = Whisky.objects.all()
    cervejas = Cerveja.objects.all()
    vinhos = Wine.objects.all()
    return render(request, 'topsellers.html', {"drinks": drinks, "vodkas": vodkas, "enlatados": enlatados, "whiskys": whiskys, "vinhos": vinhos, "cervejas": cervejas})

