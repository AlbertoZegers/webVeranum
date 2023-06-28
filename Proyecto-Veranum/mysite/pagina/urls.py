from . import views
from .views import home, exit
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('inicio', views.inicio, name='inicio'),
    path('review', views.review, name="review"),
    path('juegos', views.juegos, name= "juegos"),
    path('registrar/', views.registrar, name="registrar"),
    path('iniciar', views.iniciar, name=  "iniciar"),
    path('Gestion_juegos', views.Gestion_juegos, name= "Gestion_juegos"),
    path('agregarJuego/', views.agregarJuego),
    path('edicionJuego/<codigo>', views.edicionJuego),  
    path('editarJuego/', views.editarJuego),
    path('eliminarJuego/<codigo>', views.eliminarJuego),
    path('logout/', exit, name='exit'),
] 