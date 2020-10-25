from django.db import models

# Create your models here.
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

    def __str__(self):
        return self.nombre

class Transportista (models.Model):
    nombre = models.CharField(max_length=60)
    rut = models.CharField(max_length=10)
    tipoLicencia = models.CharField(max_length=1)

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
