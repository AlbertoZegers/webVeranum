from . import views
from .views import home, exit
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('inicio', views.inicio, name='inicio'),
    path('habitaciones', views.review, name="review"),
    path('list_habitaciones', views.juegos, name= "juegos"),
    path('registrar/', views.registrar, name="registrar"),
    path('iniciar', views.iniciar, name=  "iniciar"),
    path('Gestion', views.Gestion_juegos, name= "Gestion_juegos"),
    path('agregar/', views.agregarJuego),
    path('edicion/<codigo>', views.edicionJuego),  
    path('editar/', views.editarJuego),
    path('eliminar/<codigo>', views.eliminarJuego),
    path('logout/', exit, name='exit'),
] 