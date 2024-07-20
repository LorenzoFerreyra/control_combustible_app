import uuid
from django.db import models
from datetime import date
from django.contrib.auth.models import User


class Empleado(models.Model):
    # Campos del modelo Empleado
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    id_empleado = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    res = models.CharField(max_length=255, verbose_name="RES", blank=True)
    ub_actual = models.CharField(max_length=255, verbose_name="UB-ACTUAL", blank=True)
    paterno = models.CharField(max_length=255, verbose_name="PATERNO")
    materno = models.CharField(max_length=255, verbose_name="MATERNO")
    nom1 = models.CharField(max_length=255, verbose_name="NOM 1")
    nom2 = models.CharField(max_length=255, null=True, blank=True, verbose_name="NOM 2")
    cargo = models.CharField(max_length=255, verbose_name="CARGO")
    nivel = models.CharField(max_length=255, verbose_name="NIVEL", blank=True)
    ingreso = models.DateField(verbose_name="INGRESO", blank=True, null=True)
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

        
class Equipo(models.Model):
    # Campo ID_ITEM con el mismo funcionamiento que id_empleado
    id_item = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)

    # Otros campos...
    numero_interno = models.CharField(max_length=100,verbose_name="N° INT.", unique=True)
    tipo_equipo = models.CharField(max_length=255, verbose_name="TIPO EQUIPO")
    sam = models.CharField(max_length=255, verbose_name="SAM", blank=True)
    nuevo_codigo = models.CharField(max_length=255, verbose_name="NUEVO COD.", blank=True)
    año = models.IntegerField(verbose_name="AÑO", blank=True, null=True)
    marca = models.CharField(max_length=255, verbose_name="MARCA")
    modelo_maquina = models.CharField(max_length=255, verbose_name="MOD. MAQ.")
    consumo_promedio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="CONSUM. PROM", blank=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name="FECHA DE ACTUALIZACION")
    ubicacion = models.CharField(max_length=255, verbose_name="UBICACIÓN")

    def __str__(self):
        return f"{self.tipo_equipo} - {self.marca} {self.modelo_maquina}"

    class Meta:
        verbose_name = "Equipo"
        verbose_name_plural = "Equipos"


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
    seccion = models.CharField(max_length=255, verbose_name="SECCION", blank=True)
    longitud_km = models.IntegerField(verbose_name="LONG. Km")
    km_inicial = models.IntegerField(verbose_name="KM INICIAL", blank=True)
    km_final = models.IntegerField(verbose_name="KM FINAL", blank=True)
    tramo = models.CharField(max_length=255, verbose_name="TRAMO")
    lugar_inicial = models.CharField(max_length=255, verbose_name="LUGAR INICIAL")
    lugar_final = models.CharField(max_length=255, verbose_name="LUGAR FINAL")
    pavimento = models.BooleanField(default=False, verbose_name="PAV.", blank=True)
    empedrado = models.BooleanField(default=False, verbose_name="EMPEDRADO", blank=True)
    ripio = models.BooleanField(default=False, verbose_name="RIPIO", blank=True)
    tierra = models.BooleanField(default=False, verbose_name="TIERRA", blank=True)

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
    unidad = models.CharField(max_length=255, verbose_name="UNIDAD", blank=True)
    produccion_diaria_min = models.FloatField(verbose_name="PRODUCC DIARIA [MIN]", blank=True)
    produccion_diaria_max = models.FloatField(verbose_name="PRODUCC DIARIA [MAX]", blank=True)
    produccion_diaria_prom = models.FloatField(verbose_name="PRODUCC DIARIA [PROM]", blank=True)
    produccion_unid_hr_prom = models.FloatField(verbose_name="PRODUCC UNID/HR [PROM]", blank=True)
    produccion_hr_unid_prom = models.FloatField(verbose_name="PRODUCC HR/UNID [PROM]", blank=True)
    camioneta = models.BooleanField(default=False, verbose_name="CAMIONETA",blank=True)
    motoniveladora = models.BooleanField(default=False, verbose_name="MOTONIVELADORA", blank=True)
    camion_aguatero = models.BooleanField(default=False, verbose_name="CAMION AGUATERO", blank=True)
    bomba_de_agua = models.BooleanField(default=False, verbose_name="BOMBA DE AGUA", blank=True)

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
        verbose_name = "Proyecto DE5"
        verbose_name_plural = "Proyectos DE5"

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

class TransaccionCombustible(models.Model):
    TIPO_CHOICES = (
        ('Ingreso', 'Ingreso'),
        ('Egreso', 'Egreso'),
    )

    SUBTIPO_CHOICES = (
        ('Ingresos propios', 'Ingresos propios'),
        ('Otros ingresos', 'Otros ingresos'),
        ('Egresos por transferencia', 'Egresos por transferencia'),
        ('Ingresos por demasía o remanencia', 'Ingresos por demasía o remanencia'),
    )

    project_link = models.ForeignKey('Proyecto_DE5', on_delete=models.CASCADE, verbose_name="Proyecto")
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, verbose_name="TIPO")
    subtipo = models.CharField(max_length=50, choices=SUBTIPO_CHOICES, verbose_name="SUBTIPO")
    fecha = models.DateField(verbose_name="FECHA")
    descripcion = models.CharField(max_length=255, verbose_name="DESCRIPCION")
    gasolina_lt = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="GASOLINA [LT]", null=True, blank=True)
    diesel_lt = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="DIESEL [LT]", null=True, blank=True)
    lubricante_15w40_gasolina = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="15W-40 Gasolina", null=True, blank=True)
    lubricante_15w40_diesel = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="15W-40 Diesel", null=True, blank=True)
    lubricante_aoh68_hidraulico = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="AOH-68 Hidraulico", null=True, blank=True)
    lubricante_85w140 = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="85W-140", null=True, blank=True)
    lubricante_80w90 = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="80W-90", null=True, blank=True)
    lubricante_mt1_10w_transm = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="MT1-10W TRANSM", null=True, blank=True)
    lubricante_tipo_a = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="TIPO A", null=True, blank=True)
    anticongelante = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="ANTICONGELANTE", null=True, blank=True)
    liquido_frenos = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="LIQUID. FRENOS", null=True, blank=True)
    grasa_rodam = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="RODAM", null=True, blank=True)
    grasa_chasis = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="GRASA CHASIS", null=True, blank=True)
    observaciones = models.CharField(max_length=255, verbose_name="OBSERVACIONES", null=True, blank=True)

    def __str__(self):
        return f"{self.fecha} - {self.descripcion}"

    class Meta:
        verbose_name = "Transacción de Combustible"
        verbose_name_plural = "Transacciones de Combustible"

class EnTransito(models.Model):
    proyecto = models.ForeignKey('Proyecto_DE5', on_delete=models.CASCADE, verbose_name="Proyecto")
    numero = models.AutoField(primary_key=True, verbose_name="Número")
    fecha = models.DateField(default=date.today, verbose_name="Fecha")
    numero_interno = models.ForeignKey(Equipo, on_delete=models.CASCADE, max_length=100, verbose_name="Número Interno")
    tipo_equipo = models.CharField(max_length=200, verbose_name="Tipo de Equipo")

    # Relacionando con el modelo Empleado para obtener el operador
    operador = models.ForeignKey(Empleado, on_delete=models.CASCADE, verbose_name="Operador", blank=True, null=True)

    gasolina_cargada = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Gasolina Cargada")
    diesel_cargado = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Diesel Cargado", blank=True, null=True)
    lubricante_15w40_gasolina = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="15W-40 Gasolina", blank=True, null=True)
    lubricante_15w40_diesel = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="15W-40 Diesel", blank=True, null=True)
    lubricante_aoh68_hidraulico = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="AOH-68 Hidráulico", blank=True, null=True)
    lubricante_85w140 = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="85W-140", blank=True, null=True)
    lubricante_80w90 = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="80W-90", blank=True, null=True)
    lubricante_mt1_10w_transm = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="MT1-10W TRANSM", blank=True, null=True)
    fluido_tipo_a = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Fluido Tipo A", blank=True, null=True)
    anticongelante_litros = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Anticongelante Litros", blank=True, null=True)
    liquido_freno = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Líquido de Freno", blank=True, null=True)
    grasa_rodamiento = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Grasa de Rodamiento", blank=True, null=True)
    grasa_chasis = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Grasa de Chasis", blank=True, null=True)
    observaciones = models.TextField(max_length=400,verbose_name="Observaciones", blank=True, null=True)

    def __str__(self):
        return f"En Transito {self.numero} - Proyecto: {self.proyecto}"

    class Meta:
        verbose_name = "En Tránsito"
        verbose_name_plural = "Datos en Tránsito"
        
