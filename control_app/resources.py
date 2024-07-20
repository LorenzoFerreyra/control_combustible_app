from import_export import resources
from .models import EnTransito

class EnTransitoResource(resources.ModelResource):
    class Meta:
        model = EnTransito
        fields = (
            'numero', 
            'fecha', 
            'numero_interno', 
            'tipo_equipo', 
            'operador', 
            'gasolina_cargada', 
            'diesel_cargado', 
            'lubricante_15w40_gasolina', 
            'lubricante_15w40_diesel', 
            'lubricante_aoh68_hidraulico', 
            'lubricante_85w140', 
            'lubricante_80w90', 
            'lubricante_mt1_10w_transm', 
            'fluido_tipo_a', 
            'anticongelante_litros', 
            'liquido_freno', 
            'grasa_rodamiento', 
            'grasa_chasis', 
            'observaciones'
        )
