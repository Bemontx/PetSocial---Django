from django.db import models
from django.contrib.auth.models import User

class Mascota(models.Model):
    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=50)
    raza = models.CharField(max_length=100)
    propietario = models.ForeignKey(User, on_delete=models.CASCADE) 


class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return self.nombre