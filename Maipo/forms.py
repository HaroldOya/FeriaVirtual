from django import forms
from django.forms import ModelForm
from .models import Productor,Producto

class PostForm(forms.ModelForm):

    class Meta:
        model = Productor
        fields = ('nombre', 'correo','rut','edad','telefono','genero','direccion','nacionalidad',)
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form'}),
            'correo': forms.TextInput(attrs={'class':'Form'}),
            'rut': forms.TextInput(attrs={'class':'Form'}),
            'edad': forms.TextInput(attrs={'class':'Form'}),
            'telefono': forms.TextInput(attrs={'class':'Form'}),
            'genero': forms.TextInput(attrs={'class':'Form'}),
            'direccion': forms.TextInput(attrs={'class':'Form'}),
            'nacionalidad': forms.TextInput(attrs={'class':'Form'}),            
        }

class ProductoForm(ModelForm):

    class Meta:
        model = Producto
        fields = ['nombre','descripcion','precio']