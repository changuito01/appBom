from django.contrib import admin
from .models import *
# Register your models here.

# Este código configura la apariencia de la lista de objetos del modelo.

class CarroAdmin(admin.ModelAdmin):
    list_display = ('unidad', 'patente', 'año')

admin.site.register(Carro, CarroAdmin)