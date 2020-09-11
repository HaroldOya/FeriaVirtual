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