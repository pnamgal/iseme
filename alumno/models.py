from __future__ import unicode_literals

from django.db import models

Class Alumno(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    dni = models.IntegerField()
    mail = models.EmailField(max_length=50)
