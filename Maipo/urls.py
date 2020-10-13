from django.urls import path 
from . import views
from .views import mostrarProducto,añadirProducto


urlpatterns = [
    path('',views.index,name='index'),
    path('galeria/',views.galeria,name='galeria'),
    path('lista_productos/', views.mostrarProducto, name='lista_productos'),
    path('añadir_producto/',views.añadirProducto, name='añadir_producto'),
    
]