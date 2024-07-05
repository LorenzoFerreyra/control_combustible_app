from django import forms
from .models import Empleado, Equipo, Ruta, Actividad

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'

class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = '__all__'
        
class RutaForm(forms.ModelForm):
    class Meta:
        model = Ruta
        fields = '__all__'

class ActividadForm(forms.ModelForm):
    class Meta:
        model = Actividad
        fields = '__all__'