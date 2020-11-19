from django.urls import path 
from . import views
from .views import mostrarProducto,añadirProducto, modificarProducto, eliminarProducto,mostrarSubasta,subastaDetalle,guardarApuesta


urlpatterns = [
    path('',views.index,name='index'),
    path('galeria/',views.galeria,name='galeria'),
    path('lista_productos/', views.mostrarProducto, name='lista_productos'),
    path('añadir_producto/',views.añadirProducto, name='añadir_producto'),
    path('registro/',views.register,name='registro'),
    path('modificar_producto/<id>/',views.modificarProducto, name='modificar_producto'),
    path('eliminar_producto/<id>/',views.eliminarProducto, name='eliminar_producto'),
    path('subasta',views.mostrarSubasta, name='subastas'),
    path('subasta_apuesta/<int:subasta_id>/',views.subastaDetalle, name='subastaDetalle'),
    path('subastaRealizada/<int:subasta_id>/',views.guardarApuesta, name='subastaGuardar'),
    
]