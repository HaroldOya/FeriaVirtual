from django.db import models
# from django.contrib.auth.models import AbstractUser
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







class Productor (models.Model):
    nombre = models.CharField(max_length=60)
    correo = models.CharField(max_length=100)
    rut = models.CharField(max_length=10)
    edad = models.CharField(max_length=3)
    telefono = models.CharField(max_length=10)
    genero = models.CharField(max_length=10)
    direccion = models.CharField(max_length=10)
    nacionalidad = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class Producto (models.Model): 
    nombre = models.CharField(max_length=15)
    descripcion = models.CharField(max_length=100)
    precio = models.IntegerField()
    Productor = models.ManyToManyField('Productor', blank=True, null=True )

    def __str__(self):
        return self.nombre

class Transportista (models.Model):
    nombre  = models.CharField(max_length=60)
    rut = models.CharField(max_length=10)
    peso_max_camion = models.IntegerField(default=12)
    peso_min_camion = models.IntegerField(default=12)
    matricula = models.CharField(max_length=6, default="AAAAAA")
    VENTAS = (('Venta Interna','Venta Interna'),('Venta Externa', 'Venta Externa'))
    tipoDeVenta = models.CharField(max_length=13,choices=VENTAS, default="Venta Interna")

    def __str__(self):
        return self.nombre

class clienteExterno (models.Model):
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
    ultimoEditor = models.ForeignKey(Transportista, on_delete=models.CASCADE, null=True, blank=True)
    DireccionEntrega = models.CharField(max_length=50, default='Contactar Productor')

    def __str__(self):
        return self.codigo
    
    