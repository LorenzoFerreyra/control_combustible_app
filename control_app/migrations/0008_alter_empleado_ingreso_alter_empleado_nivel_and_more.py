# Generated by Django 4.1.2 on 2024-07-11 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control_app', '0007_empleado_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='ingreso',
            field=models.DateField(blank=True, verbose_name='INGRESO'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='nivel',
            field=models.CharField(blank=True, max_length=255, verbose_name='NIVEL'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='res',
            field=models.CharField(blank=True, max_length=255, verbose_name='RES'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='ub_actual',
            field=models.CharField(blank=True, max_length=255, verbose_name='UB-ACTUAL'),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='año',
            field=models.IntegerField(blank=True, null=True, verbose_name='AÑO'),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='consumo_promedio',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, verbose_name='CONSUM. PROM'),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='fecha_actualizacion',
            field=models.DateTimeField(auto_now=True, verbose_name='FECHA DE ACTUALIZACION'),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='nuevo_codigo',
            field=models.CharField(blank=True, max_length=255, verbose_name='NUEVO COD.'),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='numero_interno',
            field=models.CharField(max_length=100, verbose_name='N° INT.'),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='sam',
            field=models.CharField(blank=True, max_length=255, verbose_name='SAM'),
        ),
    ]