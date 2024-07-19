from django import forms
from .models import Empleado, Equipo, Ruta, Actividad, EnTransito
from django.utils.translation import gettext_lazy as _


FORM_FIELD_REQUIRED_MESSAGE = _("Este campo es obligatorio.")

class CustomForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, (forms.CharField, forms.DateField, forms.IntegerField)):
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
        fields = ['numero_interno', 'tipo_equipo', 'sam', 'nuevo_codigo','año', 'marca', 'modelo_maquina',
                  'consumo_promedio', 'ubicacion']
        
class RutaForm(CustomForm):
    class Meta:
        model = Ruta
        fields = ['ruta', 'distrito','zona', 'seccion', 'longitud_km','km_inicial', 'km_final', 'tramo','lugar_inicial','lugar_final',
                  'pavimento', 'empedrado','ripio', 'tierra']

class ActividadForm(CustomForm):
    class Meta:
        model = Actividad
        fields = '__all__'
        
class EnTransitoForm(forms.ModelForm):
    class Meta:
        model = EnTransito
        fields = '__all__'
        widgets = {
            'proyecto': forms.Select(attrs={'class': 'form-control'}),
            'numero_interno': forms.Select(attrs={'class': 'form-control'}),
            'tipo_equipo': forms.TextInput(attrs={'class': 'form-control'}),
            'operador': forms.Select(attrs={'class': 'form-control'}),
            'gasolina_cargada': forms.NumberInput(attrs={'class': 'form-control'}),
            'diesel_cargado': forms.NumberInput(attrs={'class': 'form-control'}),
            'lubricante_15w40_gasolina': forms.NumberInput(attrs={'class': 'form-control'}),
            'lubricante_15w40_diesel': forms.NumberInput(attrs={'class': 'form-control'}),
            'lubricante_aoh68_hidraulico': forms.NumberInput(attrs={'class': 'form-control'}),
            'lubricante_85w140': forms.NumberInput(attrs={'class': 'form-control'}),
            'lubricante_80w90': forms.NumberInput(attrs={'class': 'form-control'}),
            'lubricante_mt1_10w_transm': forms.NumberInput(attrs={'class': 'form-control'}),
            'fluido_tipo_a': forms.NumberInput(attrs={'class': 'form-control'}),
            'anticongelante_litros': forms.NumberInput(attrs={'class': 'form-control'}),
            'liquido_freno': forms.NumberInput(attrs={'class': 'form-control'}),
            'grasa_rodamiento': forms.NumberInput(attrs={'class': 'form-control'}),
            'grasa_chasis': forms.NumberInput(attrs={'class': 'form-control'}),
            'observaciones': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }