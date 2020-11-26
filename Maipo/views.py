from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth import login
from .models import Productor,Producto,subasta, User
from .forms import ProductorLoginForm, TransportistaLoginForm, ProductoForm
from django.shortcuts import redirect
from django.contrib.auth import logout as do_logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test, login_required
from django.views.generic import CreateView, ListView, UpdateView
from cart.cart import Cart
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html' )

def registrosAdmin(request):
    return render(request, 'registration/registros.html')

class ProductorRegistro(CreateView):
    model = User
    form_class = ProductorLoginForm
    template_name = 'registration/registro_productor.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'productor'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')

class TransportistaRegistro(CreateView):
    model = User
    form_class = TransportistaLoginForm
    template_name = 'registration/registro_transportista.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'transportista'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')



def galeria(request):
    return render(request, 'templates/galeria.html' )

def mostrarProducto(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'lista_productos.html',data)

def mostrarProductoPropios(request):
    productos = Producto.objects.filter(Productor = Productor.objects.get(user = request.user))
    data = {
        'productos': productos
    }
    return render(request, 'mis_productos.html',data)


def añadirProducto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            thought = form.save(commit=False)
            thought.Productor = Productor.objects.get(user = request.user)
            thought.save()
            return redirect(to='mis_productos')
    else:
        form = ProductoForm()
    return render(request, 'añadir_producto.html', {
        'form': form
    })

# def añadirProductohtml(request):
#     return render(request, 'añadir_producto.html')

# def añadirProducto(request):
#     txtNombre = request.POST['txtNombreProducto']
#     txtDescripcion = request.POST['txtDescripcion']
#     precio = request.POST['txtPrecio']
#     imagen = request.FILES['img']
#     user = request.session.get('user')
#     user.
#     p = Producto(Productor.user, name = txtNombre, descripcion = txtDescripcion ,price = precio, image = imagen)
#     p.save()
#     return render(request, 'index.html', {'productos':txtNombre})


def modificarProducto(request, id):
    producto = Producto.objects.get(id=id)
    data = {
        'form': ProductoForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = ProductoForm(data = request.POST, instance=producto)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Producto modificado"
            data['form'] = formulario
        else:
            data['mensaje'] = "Ha ocurrido un error"
    return render(request, 'modificar_producto.html', data )


def eliminarProducto(request, id):

    producto = Producto.objects.get(id=id)
    producto.delete()

    return redirect(to='mis_productos')

# def register(request):
#     form = UserCreationForm()
#     if request.method == "POST":
#         form = UserCreationForm(data=request.POST)
#         if form.is_valid():
#             user = form.save()
#             if user is not None:
#                 do_login(request, user)
#                 return redirect('/')
#     return render(request, "registration/registro.html", {'form': form})

@login_required
def mostrarSubasta(request):
    subasta1 = subasta.objects.all()
    data = {
        'subasta': subasta1
    }
    return render(request, 'subasta.html',data)
@login_required
def subastaDetalle(request, subasta_id):
    subasta1 = subasta.objects.get(id=subasta_id)
    dato = {
        'subastaDatos': subasta1
    }
    subasta1.vistas = subasta1.vistas + 1
    subasta1.save()
    return render(request, 'subasta_apuesta.html',dato)

@login_required
def guardarApuesta(request,subasta_id):
    current_user = request.user
    subasta1 = subasta.objects.get(id=subasta_id)
    subasta1.ultimaApuesta = request.POST['apuesta']
    subasta1.ultimoEditor = current_user
    subasta1.save()
    return render(request, 'subastaRealizada.html')

# Carro de compras

@login_required
def cart_add(request, id):
    cart = Cart(request)
    product = Producto.objects.get(id=id)
    cart.add(product=product)
    return redirect("lista_productos")


@login_required
def item_clear(request, id):
    cart = Cart(request)
    product = Producto.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required
def item_increment(request, id):
    cart = Cart(request)
    product = Producto.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required
def item_decrement(request, id):
    cart = Cart(request)
    product = Producto.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required
def cart_detail(request):
    return render(request, 'cart_detail.html')