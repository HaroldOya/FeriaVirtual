from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
# class Role(models.Model):

#   PRODUCTOR = 1
#   CLIENTE_EXTERNO = 2
#   CLIENTE_INTERNO = 3
#   TRANSPORTISTA = 4
#   CONSULTOR = 5
#   ROLE_CHOICES = (
#       (PRODUCTOR, 'productor'),
#       (CLIENTE_EXTERNO, 'clienteexterno'),
#       (CLIENTE_INTERNO, 'clienteinterno'),
#       (TRANSPORTISTA, 'transportista'),
#       (CONSULTOR, 'consultor'),
#   )

#   id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True)

#   def __str__(self):
#       return self.get_id_display()


# class User(AbstractUser):
#   roles = models.ManyToManyField(Role)

class User(AbstractUser):
    is_clienteExterno = models.BooleanField(default=False)
    is_clienteInterno = models.BooleanField(default=False)
    is_productor = models.BooleanField(default=False)
    is_transportista = models.BooleanField(default=False)
    is_consultor = models.BooleanField(default=False)


class Productor (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    nombre = models.CharField(max_length=60)
    correo = models.EmailField(max_length=254)
    rut = models.CharField(max_length=10)
    edad = models.CharField(max_length=3)
    telefono = models.CharField(max_length=10)
    genero = models.CharField(max_length=10)
    direccion = models.CharField(max_length=500)
    nacionalidad = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class Producto (models.Model): 
    descripcion = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='.\static\img\products')
    price = models.FloatField()
    Productor = models.ForeignKey(Productor,on_delete=models.PROTECT, blank=True, null=True )

    def __str__(self):
        return self.name

class Transportista (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    nombre  = models.CharField(max_length=60)
    correo = models.EmailField(max_length=254)
    rut = models.CharField(max_length=10)
    telefono = models.IntegerField()
    peso_max_camion = models.IntegerField(default=12)
    peso_min_camion = models.IntegerField(default=12)
    matricula = models.CharField(max_length=6, default="AAAAAA")
    VENTAS = (('Venta Interna','Venta Interna'),('Venta Externa', 'Venta Externa'))
    tipoDeVenta = models.CharField(max_length=13,choices=VENTAS, default="Venta Interna")

    def __str__(self):
        return self.nombre

class clienteExterno (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    nombre = models.CharField(max_length=60)
    rut = models.CharField(max_length=10)
    pais = models.CharField(max_length=15)
    region = models.CharField(max_length=40)
    ciudad = models.CharField(max_length=60)
    codigopostal = models.IntegerField()

    def __str__(self):
        return self.nombre
        return self.pais

class clienteLocal (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    nombre = models.CharField(max_length=60)
    rut = models.CharField(max_length=10)
    region = models.CharField(max_length=40)
    ciudad = models.CharField(max_length=60)

    def __str__(self):
        return self.nombre

class subasta (models.Model):
    codigo = models.CharField(max_length=5)
    productos = models.ManyToManyField(Producto)
    productor = models.ForeignKey(Productor, on_delete=models.CASCADE)
    precioInicial = models.IntegerField()
    ultimaApuesta = models.IntegerField(null=True)
    pesoProductos = models.IntegerField()
    vistas = models.IntegerField()
    ultimoEditor = models.ForeignKey(User, on_delete=models.SET(User), null=True, blank=True)
    direccionEntrega = models.CharField(max_length=50, default='Contactar Productor')
    fechaInicio = models.DateField(auto_now=True, auto_now_add=False)
    fechaTermino = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.codigo
    
    