from django import forms
from .models import Empleado, Equipo, Ruta, Actividad
from django.utils.translation import gettext_lazy as _


FORM_FIELD_REQUIRED_MESSAGE = _("Este campo es obligatorio.")

class CustomForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, (forms.CharField, forms.DateField)):
                field.error_messages['required'] = FORM_FIELD_REQUIRED_MESSAGE


class EmpleadoForm(CustomForm):
    class Meta:
        model = Empleado
        fields = ['res', 'ub_actual', 'paterno', 'materno', 'nom1', 'nom2', 'cargo', 'nivel', 'ingreso', 'salida']
        widgets = {
            'ingreso': forms.DateInput(attrs={'type': 'date'}),
            'salida': forms.DateInput(attrs={'type': 'date'}),
        }

class EquipoForm(CustomForm):
    class Meta:
        model = Equipo
        fields = '__all__'
        
class RutaForm(CustomForm):
    class Meta:
        model = Ruta
        fields = '__all__'

class ActividadForm(CustomForm):
    class Meta:
        model = Actividad
        fields = '__all__'