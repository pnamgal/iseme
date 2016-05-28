from __future__ import unicode_literals

from django.db import models

Class Administrador(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    mail = models.EmailField(max_length=50)
