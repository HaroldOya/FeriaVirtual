from django.urls import path 
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('galeria/',views.galeria,name='galeria'),
    path('register/', views.register, name='formulario'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='salir'),


]