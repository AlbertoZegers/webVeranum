from django.shortcuts import render, redirect
from .models import Juego
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import JuegoForm, UsuarioForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


#APLICACION
def home(request):
    return render(request, "index.html")
def inicio(request):
    return render(request, "index.html")

def review(request):
    return render(request, "paginas/review.html")

def juegos(request):
    juegos = Juego.objects.all()
    return render(request, "paginas/Juegos.html", {"juegos": juegos})

def registrar(request):
    return render(request, "registration/register.html")

@login_required
def iniciar(request):
    if request.user.is_authenticated:
        return redirect('home')
    return render(request, "registration/login.html")

def exit(request):
    logout(request)
    return redirect('home')

def Gestion_juegos(request):
    juegos = Juego.objects.all()
    return render(request, "paginas/GestionJuegos.html", {"juegos": juegos})


def agregarJuego(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    descripcion = request.POST['txtDesc']
    juego = Juego.objects.create(codigo=codigo,nombre=nombre, descripcion=descripcion)
    messages.success(request, '¡Juego Agregado Correctamente!')
    return redirect('Gestion_juegos')

def edicionJuego(request, codigo):
    juegos = Juego.objects.get(codigo=codigo)
    return render(request, "paginas/editarJuego.html", {"juegos": juegos})

def eliminarJuego(request, codigo):
    juegos = Juego.objects.get(codigo=codigo)
    juegos.delete()
    return redirect('Gestion_juegos')

def editarJuego(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    descripcion = request.POST['txtDesc']
    juegos = Juego.objects.get(codigo=codigo)
    juegos.codigo = codigo
    juegos.nombre = nombre
    juegos.descripcion = descripcion
    juegos.save()
    return redirect('Gestion_juegos')

#LOGEO Y REGISTRAR USUARIOS
