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