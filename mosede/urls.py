from django.urls import path
from django.contrib import admin
from . import views
from .views import index

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index.as_view(), name='index'),
    path('homepage', views.homepage, name='homepage'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('vinhos', views.vinhos, name='vinhos'),
    path('cervejas', views.cervejas, name='cervejas'),
    path('whiskys', views.whiskys, name='whiskys'),
    path('enlatados', views.enlatados, name='enlatados'),
    path('vodkas', views.vodkas, name='vodkas'),
    path('drinks', views.drinks, name='drinks'),
    path('topsellers', views.topsellers, name='topsellers'),
]