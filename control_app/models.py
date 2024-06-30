from django.db import models

class Empleado(models.Model):
    # Campos del modelo Empleado
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
