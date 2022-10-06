from unittest.util import _MAX_LENGTH
from django.db import models

class Contacto(models.Model):
    nombre = models.CharField(max_length = 100)
    apellido = models.CharField(max_length = 100)
    telefono = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)

    def __str__(self):
        return self.nombre
    
   