import uuid
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

class Empleado(models.Model):
    # Campos del modelo Empleado
    id_empleado = models.CharField(max_length=10, unique=True, editable=False, null=True)
    res = models.CharField(max_length=255, verbose_name="RES")
    ub_actual = models.CharField(max_length=255, verbose_name="UB-ACTUAL")
    paterno = models.CharField(max_length=255, verbose_name="PATERNO")
    materno = models.CharField(max_length=255, verbose_name="MATERNO")
    nom1 = models.CharField(max_length=255, verbose_name="NOM 1")
    nom2 = models.CharField(max_length=255, null=True, blank=True, verbose_name="NOM 2")
    cargo = models.CharField(max_length=255, verbose_name="CARGO")
    nivel = models.CharField(max_length=255, verbose_name="NIVEL")
    ingreso = models.DateField(verbose_name="INGRESO")
    salida = models.DateField(null=True, blank=True, verbose_name="SALIDA")
    admin = models.BooleanField(default=False, verbose_name="Admin")

    @property
    def completo(self):
        # Usamos el decorador property para armar el nombre completo del empleado
        # a partir de otros campos
        nombres = [self.paterno, self.materno, self.nom1]
        if self.nom2:
            nombres.append(self.nom2)
        return ' '.join(nombres)

    def __str__(self):
        # Representación del objeto Empleado
        return f"{self.paterno} {self.materno}, {self.nom1} {self.nom2 if self.nom2 else ''}"

    # En Meta aclaramos y hacemos mas amigables los metadatos para observarlos mejor en el admin site
    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"

# Función para generar el id_empleado único
def generate_unique_id_empleado():
    return uuid.uuid4().hex[:10].upper()

# Conectar la señal pre_save al modelo Empleado
@receiver(pre_save, sender=Empleado)
def set_unique_id_empleado(sender, instance, **kwargs):
    if not instance.id_empleado:
        instance.id_empleado = generate_unique_id_empleado()
        
class Equipo(models.Model):
    # Campo ID_ITEM con el mismo funcionamiento que id_empleado
    id_item = models.CharField(max_length=10, unique=True, editable=False)

    # Otros campos...
    numero_interno = models.IntegerField(verbose_name="N° INT.")
    tipo_equipo = models.CharField(max_length=255, verbose_name="TIPO EQUIPO")
    sam = models.CharField(max_length=255, verbose_name="SAM")
    nuevo_codigo = models.CharField(max_length=255, verbose_name="NUEVO COD.")
    año = models.IntegerField(verbose_name="AÑO")
    marca = models.CharField(max_length=255, verbose_name="MARCA")
    modelo_maquina = models.CharField(max_length=255, verbose_name="MOD. MAQ.")
    consumo_promedio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="CONSUM. PROM")
    fecha_actualizacion = models.DateField(verbose_name="FECHA DE ACTUALIZACION")
    ubicacion = models.CharField(max_length=255, verbose_name="UBICACIÓN")

    def __str__(self):
        return f"{self.tipo_equipo} - {self.marca} {self.modelo_maquina}"

    class Meta:
        verbose_name = "Equipo"
        verbose_name_plural = "Equipos"

def generate_unique_id_item():
    return uuid.uuid4().hex[:10].upper()
# Conectamos la señal pre_save al modelo Equipo
@receiver(pre_save, sender=Equipo)
def set_unique_id_item(sender, instance, **kwargs):
    if not instance.id_item:
        instance.id_item = generate_unique_id_item()

class Ruta(models.Model):
    # Campos del modelo Ruta
    ruta = models.CharField(max_length=255, verbose_name="RUTA")
    distrito = models.IntegerField(verbose_name="DISTRITO")
    ZONA_CHOICES = [
        ('Chaco', 'Chaco'),
        ('Centro', 'Centro'),
        ('Cintis', 'Cintis'),
        ('Norte', 'Norte'),
    ]
    zona = models.CharField(max_length=10, choices=ZONA_CHOICES, verbose_name="ZONA")
    seccion = models.CharField(max_length=255, verbose_name="SECCION")
    longitud_km = models.IntegerField(verbose_name="LONG. Km")
    km_inicial = models.IntegerField(verbose_name="KM INICIAL")
    km_final = models.IntegerField(verbose_name="KM FINAL")
    tramo = models.CharField(max_length=255, verbose_name="TRAMO")
    lugar_inicial = models.CharField(max_length=255, verbose_name="LUGAR INICIAL")
    lugar_final = models.CharField(max_length=255, verbose_name="LUGAR FINAL")
    pavimento = models.BooleanField(default=False, verbose_name="PAV.")
    empedrado = models.BooleanField(default=False, verbose_name="EMPEDRADO")
    ripio = models.BooleanField(default=False, verbose_name="RIPIO")
    tierra = models.BooleanField(default=False, verbose_name="TIERRA")

    def __str__(self):
        return self.ruta

    class Meta:
        verbose_name = "Ruta"
        verbose_name_plural = "Rutas"
        
class Actividad(models.Model):
    # Campo N° (id autoincremental de Django)
    id = models.AutoField(primary_key=True, verbose_name="N°")
    
    # Otros campos
    codigo = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="CODIGO")
    grupo = models.IntegerField(verbose_name="GRUPO")
    actividad = models.CharField(max_length=255, verbose_name="ACTIVIDAD")
    subactividad = models.CharField(max_length=255, verbose_name="SUBACTIVIDAD")
    unidad = models.CharField(max_length=255, verbose_name="UNIDAD")
    produccion_diaria_min = models.FloatField(verbose_name="PRODUCC DIARIA [MIN]")
    produccion_diaria_max = models.FloatField(verbose_name="PRODUCC DIARIA [MAX]")
    produccion_diaria_prom = models.FloatField(verbose_name="PRODUCC DIARIA [PROM]")
    produccion_unid_hr_prom = models.FloatField(verbose_name="PRODUCC UNID/HR [PROM]")
    produccion_hr_unid_prom = models.FloatField(verbose_name="PRODUCC HR/UNID [PROM]")
    camioneta = models.BooleanField(default=False, verbose_name="CAMIONETA")
    motoniveladora = models.BooleanField(default=False, verbose_name="MOTONIVELADORA")
    camion_aguatero = models.BooleanField(default=False, verbose_name="CAMION AGUATERO")
    bomba_de_agua = models.BooleanField(default=False, verbose_name="BOMBA DE AGUA")

    def __str__(self):
        return self.actividad

    class Meta:
        verbose_name = "Actividad"
        verbose_name_plural = "Actividades"