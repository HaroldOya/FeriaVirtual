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

class Cliente_Interno (models.Model):
    nombre: models.CharField(max_length=60)
    apellido: models.CharField(max_length=60)
    correo: models.CharField(max_length=40)
    rut: models.CharField(max_length=10)
    region: models.CharField(max_length=30)
    
    def __str__(self):
        return self.nombre

class Cliente_Externo (models.Model):
    nombre: models.CharField(max_length=60)
    apellido: models.CharField(max_length=60)
    correo: models.CharField(max_length=40)
    rut: models.CharField(max_length=10)
    pais: models.CharField(max_length=15)
    region: models.CharField(max_length=30)
    ciudad: models.CharField(max_length=40)
    codigoPostal: models.IntegerField()
    
    def __str__(self):
        return self.nombre

class Transportista (models.Model):
    nombre: models.CharField(max_length=60)
    apellido: models.CharField(max_length=60)
    rut: models.CharField(max_length=10)
    tipoLicencia: models.CharField(max_length=1)
    numeroContacto: models.IntegerField()

    def __str__(self):
        return self.nombre

class Producto (models.Model):
    nombreProducto = models.CharField(max_length=20)
    cantidad = models.IntegerField()
    precio = models.IntegerField()
    descripcion = models.TextField()
    dueñoProducto = models.ForeignKey(Productor, on_delete=models.CASCADE)
    fechaPublicacion = models.DateTimeField()

    def __str__(self):
        return self.nombreProducto

