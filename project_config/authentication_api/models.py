from pickle import TRUE
from pyexpat import model
from venv import create
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Prueba_modelo(models.Model):
    nombre = models.CharField(max_length=50, blank=False, null=False)
    apellido = models.CharField(max_length=50, blank=False, null=False)
    correo = models.EmailField(max_length=50, blank=False, null=False)
    fecha_de_creacion = models.DateTimeField(auto_now_add=True)
    


    
    