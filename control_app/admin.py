from django.contrib import admin
from .models import Empleado, Equipo, Ruta, Actividad, Proyecto_DE5, ControlMensualEquipo, TransaccionCombustible, EnTransito

admin.site.register(ControlMensualEquipo)
admin.site.register(Empleado)
admin.site.register(Equipo)
admin.site.register(Ruta)
admin.site.register(Actividad)
admin.site.register(Proyecto_DE5)
admin.site.register(TransaccionCombustible)
admin.site.register(EnTransito)
