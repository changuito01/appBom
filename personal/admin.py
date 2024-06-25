from django.contrib import admin
from .models import *

# Este código configura la apariencia y funcionalidad de la interfaz de administración de Django para el modelo Bombero.

class BomberoAdmin(admin.ModelAdmin):
    list_display = ('rango', 'rut', 'nombres', 'apellido_paterno')
    search_fields = ('rut', 'apellido_paterno')

# Register your models here.

admin.site.register(Bombero, BomberoAdmin)