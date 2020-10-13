from django.shortcuts import render
from django.utils import timezone
from .models import Productor,Producto
from .forms import PostForm,ProductoForm
from django.shortcuts import redirect
from django.contrib.auth import logout as do_logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def index(request):
    return render(request, 'index.html' )


def galeria(request):
    return render(request, 'templates/galeria.html' )

def mostrarProducto(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'lista_productos.html',data)


def añadirProducto(request):
    data = {
        'form': ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Producto almacenado"
    return render(request, 'añadir_producto.html',data )