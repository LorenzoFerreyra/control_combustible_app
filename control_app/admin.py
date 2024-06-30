from django.contrib import admin
from .models import ControlMensualEquipo

class ControlMensualEquipoAdmin(admin.ModelAdmin):
    readonly_fields = ('horas_operadas', 'dia')  # Campos que no se pueden editar
    list_display = ('fecha', 'codigo_operacion', 'horas_operadas', 'dia')  # Campos que se muestran en la lista

admin.site.register(ControlMensualEquipo, ControlMensualEquipoAdmin)
