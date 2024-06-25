from django.db import models

# Create your models here.

# Estos campos definen la estructura de la base de datos para almacenar información relacionada con carros, como su unidad, patente y año.

class Carro(models.Model):
    unidad = models.CharField(max_length=100, verbose_name='Unidad')
    patente = models.CharField(max_length=20, verbose_name='Patente')
    año = models.PositiveIntegerField(verbose_name='Año')


    # Método que se utiliza para proporcionar una representación en forma de cadena.
    def __str__(self):
        return f'{self.unidad} {self.patente}'