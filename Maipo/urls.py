from django.urls import path 
from . import views
from .views import mostrarProducto,añadirProducto


urlpatterns = [
    path('',views.index,name='index'),
    path('galeria/',views.galeria,name='galeria'),
    path('register/', views.register, name='formulario'),
    path('login/', views.login, name='login'),
    path('lista_productos/', views.mostrarProducto, name='lista_productos'),
    path('logout/', views.logout, name='salir'),
    path('añadir_producto/',views.añadirProducto, name='añadir_producto'),
    
]