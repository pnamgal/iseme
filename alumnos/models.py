from __future__ import unicode_literals
from carreras.models import Carrera
from django.db import models

class Alumno(models.Model):
    name = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    dni = models.IntegerField()
    Ciudad = models.CharField(max_length=255)
    imagen = models.ImageField(blank=True)
    carrera = models.ForeignKey(Carrera)

    def __str__(self):
        return self.name
