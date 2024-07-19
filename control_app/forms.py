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
    numero_interno = forms.ModelChoiceField(
        queryset=Equipo.objects.all(),
        label="Número Interno",
        empty_label="Seleccione un número interno"
    )

    class Meta:
        model = EnTransito
        fields = ['proyecto', 'numero_interno', 'tipo_equipo', 'operador', 'gasolina_cargada', 'diesel_cargado', 
                  'lubricante_15w40_gasolina', 'lubricante_15w40_diesel', 
                  'lubricante_aoh68_hidraulico', 'lubricante_85w140', 'lubricante_80w90', 
                  'lubricante_mt1_10w_transm', 'fluido_tipo_a', 'anticongelante_litros', 
                  'liquido_freno', 'grasa_rodamiento', 'grasa_chasis', 'observaciones']
        widgets = {
            'proyecto': forms.Select(attrs={'class': 'form-control'}),
            'tipo_equipo': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['numero_interno'].widget.attrs.update({'class': 'form-control'})
        self.fields['numero_interno'].queryset = Equipo.objects.all().order_by('numero_interno')
        self.fields['numero_interno'].label_from_instance = self.label_from_instance
        self.fields['tipo_equipo'].required = False

    @staticmethod
    def label_from_instance(obj):
        return f"{obj.numero_interno} - {obj.tipo_equipo}"

    def clean(self):
        cleaned_data = super().clean()
        numero_interno = cleaned_data.get('numero_interno')
        if numero_interno:
            cleaned_data['tipo_equipo'] = numero_interno.tipo_equipo
        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)
        if instance.numero_interno:
            instance.tipo_equipo = instance.numero_interno.tipo_equipo
        if commit:
            instance.save()
        return instance