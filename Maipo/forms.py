from django import forms
from django.forms import ModelForm
from django.db import transaction
from django.contrib.auth.forms import UserCreationForm
from .models import Productor,Producto, subasta, User, Transportista, clienteLocal, clienteExterno
from django.core.validators import MaxValueValidator
from django_countries.widgets import CountrySelectWidget
from django_countries.fields import CountryField
from localflavor.cl.forms import CLRegionSelect, CLRutField

# class PostForm(forms.ModelForm):

#     class Meta:
#         model = Productor
#         fields = ('nombre', 'correo','rut','edad','telefono','genero','direccion','nacionalidad',)
#         widgets = {
#             'nombre': forms.TextInput(attrs={'class':'form'}),
#             'correo': forms.TextInput(attrs={'class':'Form'}),
#             'rut': forms.TextInput(attrs={'class':'Form'}),
#             'edad': forms.TextInput(attrs={'class':'Form'}),
#             'telefono': forms.TextInput(attrs={'class':'Form'}),
#             'genero': forms.TextInput(attrs={'class':'Form'}),
#             'direccion': forms.TextInput(attrs={'class':'Form'}),
#             'nacionalidad': forms.TextInput(attrs={'class':'Form'}),            
#         }

class ClienteInternoLoginForm(UserCreationForm):
    
    nombre = forms.CharField(label="Nombre",max_length=100, required=True)
    correo = forms.EmailField(label="Correo Electronico", required=True)
    rut = CLRutField()
    telefono = forms.IntegerField(validators=[MaxValueValidator(999999999)], required=True)
    REGION_CHOICES = (('RM', 'Región Metropolitana de Santiago'), ('I', 'Región de Tarapacá'), ('II', 'Región de Antofagasta'), ('III', 'Región de Atacama'), ('IV', 'Región de Coquimbo'), ('V', 'Región de Valparaíso'), ('VI', 'Región del Libertador Bernardo O^Higgins'), ('VII', 'Región del Maule'), ('VIII', 'Región del Bío Bío'), ('IX', 'Región de la Araucanía'), ('X', 'Región de los Lagos'), ('XI', 'Región de Aysén del General Carlos Ibáñez del Campo'), ('XII', 'Región de Magallanes y la Antártica Chilena'), ('XIV', 'Región de Los Ríos'), ('XV', 'Región de Arica-Parinacota'))
    regiones = forms.ChoiceField(choices=REGION_CHOICES)
    comuna = forms.CharField(max_length=500, required=False)
    codigopostal = forms.IntegerField(required=False)
    
    class Meta:
        model = User
        fields = ('username','nombre','correo','rut','telefono','regiones','comuna','codigopostal')
        
    @transaction.atomic
    def save(self):
        user = super(ClienteInternoLoginForm, self).save(commit=False)
        user.is_clienteInterno = True
        user.save()
        clienteInterno = clienteLocal.objects.create(user=user, nombre = self.cleaned_data["nombre"],regiones = self.cleaned_data["regiones"], correo = self.cleaned_data["correo"], rut = self.cleaned_data["rut"],
            telefono = self.cleaned_data["telefono"],comuna = self.cleaned_data["comuna"],codigopostal = self.cleaned_data["codigopostal"])
        return user


class ProductorLoginForm(UserCreationForm):
    
    nombre = forms.CharField(label="Nombre",max_length=100, required=True)
    correo = forms.EmailField(label="Correo Electronico", required=True)
    rut = forms.CharField(max_length=100, required=True)
    edad = forms.IntegerField(required=False)
    telefono = forms.CharField(max_length=100, required=True)

    GENEROS = [
    ('femenino', 'Femenino'),
    ('masculino', 'Masculino'),
    ('sin_especificar', 'Sin Especificar'),
    ]

    genero = forms.CharField(widget=forms.Select(choices=GENEROS))
    nacionalidad = CountryField().formfield()
    direccion = forms.CharField(max_length=100, required=True)

    class Meta:
        model = User
        fields = ('username','nombre','correo','rut','edad','telefono','genero','nacionalidad','direccion')

    @transaction.atomic
    def save(self):
        user = super(ProductorLoginForm, self).save(commit=False)
        user.is_productor = True
        user.save()
        productor = Productor.objects.create(user=user, nombre = self.cleaned_data["nombre"], correo = self.cleaned_data["correo"], rut = self.cleaned_data["rut"],
            edad = self.cleaned_data["edad"], telefono = self.cleaned_data["telefono"], genero = self.cleaned_data["genero"], nacionalidad = self.cleaned_data["nacionalidad"],
            direccion = self.cleaned_data["direccion"])
        return user

class TransportistaLoginForm(UserCreationForm):
    
    nombre = forms.CharField(label="Nombre",max_length=100, required=True)
    correo = forms.EmailField(label="Correo Electronico", required=True)
    rut = forms.CharField(max_length=100, required=True)
    telefono = forms.IntegerField(validators=[MaxValueValidator(999999999)], required=True)
    peso_max_camion = forms.IntegerField(required=True)
    peso_min_camion = forms.IntegerField(required=True)
    matricula = forms.CharField(max_length=6)
    nacionalidad = CountryField().formfield()
    VENTAS = (('Venta Interna','Venta Interna'),('Venta Externa', 'Venta Externa'))
    tipoDeVenta = forms.ChoiceField(choices=VENTAS)

    class Meta:
        model = User
        fields = ('username','nombre','correo','rut','telefono','peso_max_camion','peso_min_camion','matricula','nacionalidad','tipoDeVenta')

    @transaction.atomic
    def save(self):
        user = super(TransportistaLoginForm, self).save(commit=False)
        user.is_transportista = True
        user.save()
        transportista = Transportista.objects.create(user=user, nombre = self.cleaned_data["nombre"], correo = self.cleaned_data["correo"], rut = self.cleaned_data["rut"],
            telefono = self.cleaned_data["telefono"],peso_max_camion = self.cleaned_data["peso_max_camion"],peso_min_camion = self.cleaned_data["peso_min_camion"],
            tipoDeVenta = self.cleaned_data["tipoDeVenta"])
        return user


class ClienteExternoLoginForm(UserCreationForm):
    
    nombre = forms.CharField(label="Nombre",max_length=100, required=True)
    correo = forms.EmailField(label="Correo Electronico", required=True)
    ID = forms.CharField(max_length=20)
    nacionalidad = CountryField().formfield()
    region = forms.CharField(label="Region",max_length=100, required=True)
    ciudad = forms.CharField(max_length=500, required=False)
    codigopostal = forms.IntegerField(required=False)

    class Meta:
        model = User
        fields = ('username','nombre','correo','ID','nacionalidad','region','ciudad','codigopostal')

    @transaction.atomic
    def save(self):
        user = super(ClienteExternoLoginForm, self).save(commit=False)
        user.is_clienteExterno = True
        user.save()
        clienteInternacional = clienteExterno.objects.create(user=user, nombre = self.cleaned_data["nombre"], correo = self.cleaned_data["correo"], ID = self.cleaned_data["ID"],
           pais = self.cleaned_data['nacionalidad'],region = self.cleaned_data["region"],ciudad = self.cleaned_data["ciudad"],codigopostal = self.cleaned_data["codigopostal"])
        return user

class ProductoForm(ModelForm):

    class Meta:
        model = Producto
        labels = {"price": "Precio","descripcion":"Descripcion","name":"Nombre", "image":"Imagen"}
        fields = ['name','descripcion','price','image']

    

    
        

