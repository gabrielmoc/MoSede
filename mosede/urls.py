from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('homepage', views.home, name='homepage'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('vinhos', views.vinhos, name='vinhos'),
    path('cervejas', views.cervejas, name='cervejas'),
    path('whiskys', views.whiskys, name='whiskys')
]