from django.db import models
from personal.models import *
from carrobomba.models import *
# Create your models here.

# Este modelo (Herramientas) está diseñado para almacenar información sobre herramientas, incluyendo detalles como el elemento, marca, observaciones, cantidad y estado.

class Herramientas(models.Model):
    elemento = models.CharField(blank=True, max_length=100, verbose_name='Elemento')
    marca = models.CharField(blank=True, max_length=100, verbose_name='Marca')
    observaciones = models.CharField(max_length=100, verbose_name='Observaciones')
    cantidad = models.PositiveIntegerField(verbose_name='Cantidad')
    estado = models.CharField(max_length=100, verbose_name='Estado')

    # Se indica que la clase que contiene esta metaclase es abstracta y no debe generar una tabla en la base de datos.
    
    class Meta:
        abstract = True

# Este modelo Inventario extiende la funcionalidad del modelo Herramientas al agregar campos específicos para gestionar inventarios, como fechas, responsables (realizado_por y revisado_por), y el carro asociado al inventario.

class Inventario(Herramientas):
    fecha = models.DateField(verbose_name='Fecha')
    fecha_entrega = models.DateField(verbose_name='Fecha de Entrega')
    fecha_revision = models.DateField(verbose_name='Fecha de Revisión')
    realizado_por = models.ForeignKey(Bombero, on_delete=models.CASCADE, verbose_name='Realizado Por', related_name='realizado_por_inventarios')
    revisado_por = models.ForeignKey(Bombero, on_delete=models.CASCADE, verbose_name='Revisado Por', related_name='revisado_por_inventarios')
    carro = models.ForeignKey(Carro , on_delete=models.CASCADE, verbose_name='Carro')

    # La implementación devuelve una cadena que combina el valor del atributo fecha y el atributo revisado_por, separados por un espacio en blanco.
    
    def __str__(self):
        return f'{self.fecha} {self.revisado_por}'
    