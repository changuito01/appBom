from django.contrib.auth.models import AbstractUser
from django.db import models
from .opciones import *


class Persona(models.Model):
    rut = models.CharField(max_length=10, unique=True, verbose_name='Rut')
    nombres = models.CharField(max_length=100, verbose_name='Nombres')
    apellido_paterno = models.CharField(max_length=100, verbose_name='Apellido Paterno')
    apellido_materno = models.CharField(max_length=100, verbose_name='Apellido Materno')
    direccion = models.CharField(max_length=100, verbose_name='Dirección')
    telefono = models.CharField(max_length=10, verbose_name='Teléfono')


    class Meta:
        abstract = True


class Bombero(Persona):
    rango = models.CharField(max_length=20, choices=opciones_rango, verbose_name='Rango')


    def __str__(self):
        return f'{self.rango} {self.nombres} {self.apellido_paterno}'
    

class UsuarioPersonalizado(AbstractUser):
    rut = models.CharField(max_length=10, unique=True, verbose_name='Rut')
    nombres = models.CharField(max_length=100, verbose_name='Nombres')
    apellido_paterno = models.CharField(max_length=100, verbose_name='Apellido Paterno')
    apellido_materno = models.CharField(max_length=100, verbose_name='Apellido Materno')
    direccion = models.CharField(max_length=100, verbose_name='Dirección')
    telefono = models.CharField(max_length=10, verbose_name='Teléfono')
    rango = models.CharField(max_length=20, choices=opciones_rango, verbose_name='Rango')