from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    dni = models.IntegerField()
    direccion = models.CharField(max_length=50)
    telefono = models.IntegerField()
    ciudad = models.CharField(max_length=50)
    provincia = models.CharField(max_length=35)
    pais = models.CharField(max_length=30)
    email = models.EmailField()

class Alumno(Persona):
    carrera = models.CharField(max_length=30)
    edad = models.CharField(max_length=15)

