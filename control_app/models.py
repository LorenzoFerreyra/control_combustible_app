import uuid
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from datetime import date

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
    ruta = models.CharField(max_length=255, verbose_name="RUTA", primary_key=True)
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

class Proyecto_DE5(models.Model):
    id_proyecto = models.AutoField(primary_key=True, verbose_name="ID de proyecto")
    nro_interno = models.CharField(max_length=255, verbose_name="N.° interno de proyecto")
    nombre = models.CharField(max_length=255, verbose_name="Nombre de Proyecto")
    provincia = models.CharField(max_length=255, verbose_name="Provincia")
    director = models.ForeignKey('Empleado', on_delete=models.CASCADE, verbose_name="Director o Encargado")
    fecha_inicio = models.DateField(verbose_name="Fecha de inicio")
    fecha_fin = models.DateField(null=True, blank=True, verbose_name="Fecha de fin")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"

class ControlMensualEquipo(models.Model):
    proyecto = models.ForeignKey('Proyecto_DE5', on_delete=models.CASCADE, verbose_name="Proyecto")
    DIA_SEMANA_CHOICES = [
        (1, 'Lunes'),
        (2, 'Martes'),
        (3, 'Miércoles'),
        (4, 'Jueves'),
        (5, 'Viernes'),
        (6, 'Sábado'),
        (7, 'Domingo'),
    ]
    dia = models.IntegerField(choices=DIA_SEMANA_CHOICES, editable=False, verbose_name="DIA")
    fecha = models.DateField(verbose_name="FECHA", default=date.today)
    codigo_operacion = models.CharField(max_length=255, verbose_name="COD. OPE.")
    tramo = models.ForeignKey('Ruta', on_delete=models.CASCADE, verbose_name="TRAMO")
    alm_5 = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="ALM-5")
    gasolina = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="GASOLINA")
    diesel = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="DIESEL")
    horometro_inicial = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="HOROMETRO INICIAL")
    horometro_final = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="HOROMETRO FINAL")
    horas_operadas = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="HORAS OPERADAS", editable=False)
    actividad = models.ForeignKey('Actividad', on_delete=models.CASCADE, verbose_name="ACTIVIDAD")
    cantidad = models.IntegerField(verbose_name="CANTIDAD")
    pasadas = models.IntegerField(verbose_name="PASADAS")
    lubricante_15w40_gasolina = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="15W-40 Gasolina")
    lubricante_15w40_diesel = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="15W-40 Diesel")
    lubricante_aoh68_hidraulico = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="AOH-68 Hidraulico")
    lubricante_85w140 = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="85W-140")
    lubricante_80w90 = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="80W-90")
    lubricante_mt1_10w_transm = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="MT1-10W TRANSM")
    lubricante_tipo_a = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="TIPO A")
    anticongelante = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="ANTICONGELANTE")
    liquido_frenos = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="LIQUID. FRENOS")
    grasa_rodam_kg = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="RODAM")
    grasa_chasis_kg = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="CHASIS")
    hrs_disponibilidad = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="HRS DISP.")
    hrs_combustible = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="HRS COMB.")
    hrs_lubricantes = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="HRS LUB.")
    hrs_repuestos = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="HRS REPU.")
    hrs_operador = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="HRS OPE.")
    hrs_tiempo = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="HRS TIEM.")
    hrs_reparacion = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="HRS REPA.")
    hrs_mantenimiento = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="HRS MTO.")
    hrs_otros = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="HRS OTROS")

    def __str__(self):
        return f"{self.fecha} - {self.codigo_operador}"

    class Meta:
        verbose_name = "Control Mensual de Equipo"
        verbose_name_plural = "Controles Mensuales de Equipos"
    
    @property
    def hrs_total_perdidas(self):
        total_perdidas = (
            self.hrs_combustible +
            self.hrs_lubricantes +
            self.hrs_repuestos +
            self.hrs_operador +
            self.hrs_tiempo +
            self.hrs_reparacion +
            self.hrs_mantenimiento +
            self.hrs_otros
        )
        return total_perdidas
    def save(self, *args, **kwargs):
        self.dia = self.fecha.isoweekday()  # Lunes es 1 y Domingo es 7
        self.horas_operadas = self.horometro_final - self.horometro_inicial
        super().save(*args, **kwargs)