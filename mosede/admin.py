from django.contrib import admin
from mosede.models import User, Buy, Wine, Cerveja, Whisky, Enlatado, Vodka, Drink

admin.site.register((User, Buy, Wine, Cerveja, Whisky, Enlatado, Vodka, Drink))
