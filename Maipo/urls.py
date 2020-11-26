from django.urls import path 
from . import views
from .views import *
from django.conf import settings

from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name='index'),
    path('galeria/',views.galeria,name='galeria'),
    path('lista_productos/', views.mostrarProducto, name='lista_productos'),
    path('añadir_producto/',views.añadirProducto, name='añadir_producto'),
    path('mis_productos',views.mostrarProductoPropios, name='mis_productos'),
    path('registros/',views.registrosAdmin,name='registros'),
    path('registros/productor',views.ProductorRegistro.as_view(),name='registro_productor'),
    path('registros/transportista',views.TransportistaRegistro.as_view(),name='registro_transportista'),
    path('modificar_producto/<id>/',views.modificarProducto, name='modificar_producto'),
    path('eliminar_producto/<id>/',views.eliminarProducto, name='eliminar_producto'),
    path('subasta',views.mostrarSubasta, name='subastas'),
    path('subasta_apuesta/<int:subasta_id>/',views.subastaDetalle, name='subastaDetalle'),
    path('subastaRealizada/<int:subasta_id>/',views.guardarApuesta, name='subastaGuardar'),
    #Carro de compra
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
        views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)