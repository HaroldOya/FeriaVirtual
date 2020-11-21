from django.urls import path 
from . import views
from .views import *


urlpatterns = [
    path('',views.index,name='index'),
    path('galeria/',views.galeria,name='galeria'),
    path('lista_productos/', views.mostrarProducto, name='lista_productos'),
    path('añadir_producto/',views.añadirProducto, name='añadir_producto'),
    path('registros/',views.registrosAdmin,name='registros'),
    path('registros/productor',views.ProductorRegistro.as_view(),name='registro_productor'),
    path('registros/transportista',views.TransportistaRegistro.as_view(),name='registro_transportista'),
    path('modificar_producto/<id>/',views.modificarProducto, name='modificar_producto'),
    path('eliminar_producto/<id>/',views.eliminarProducto, name='eliminar_producto'),
    path('subasta',views.mostrarSubasta, name='subastas'),
    path('subasta_apuesta/<int:subasta_id>/',views.subastaDetalle, name='subastaDetalle'),
    path('subastaRealizada/<int:subasta_id>/',views.guardarApuesta, name='subastaGuardar')
]