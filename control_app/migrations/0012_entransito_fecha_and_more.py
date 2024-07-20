# Generated by Django 4.1.2 on 2024-07-20 02:16

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('control_app', '0011_alter_actividad_bomba_de_agua_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='entransito',
            name='fecha',
            field=models.DateField(default=datetime.date.today, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='entransito',
            name='anticongelante_litros',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Anticongelante Litros'),
        ),
        migrations.AlterField(
            model_name='entransito',
            name='diesel_cargado',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Diesel Cargado'),
        ),
        migrations.AlterField(
            model_name='entransito',
            name='fluido_tipo_a',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Fluido Tipo A'),
        ),
        migrations.AlterField(
            model_name='entransito',
            name='grasa_chasis',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Grasa de Chasis'),
        ),
        migrations.AlterField(
            model_name='entransito',
            name='grasa_rodamiento',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Grasa de Rodamiento'),
        ),
        migrations.AlterField(
            model_name='entransito',
            name='liquido_freno',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Líquido de Freno'),
        ),
        migrations.AlterField(
            model_name='entransito',
            name='lubricante_15w40_diesel',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='15W-40 Diesel'),
        ),
        migrations.AlterField(
            model_name='entransito',
            name='lubricante_15w40_gasolina',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='15W-40 Gasolina'),
        ),
        migrations.AlterField(
            model_name='entransito',
            name='lubricante_80w90',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='80W-90'),
        ),
        migrations.AlterField(
            model_name='entransito',
            name='lubricante_85w140',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='85W-140'),
        ),
        migrations.AlterField(
            model_name='entransito',
            name='lubricante_aoh68_hidraulico',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='AOH-68 Hidráulico'),
        ),
        migrations.AlterField(
            model_name='entransito',
            name='lubricante_mt1_10w_transm',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='MT1-10W TRANSM'),
        ),
        migrations.AlterField(
            model_name='entransito',
            name='numero_interno',
            field=models.CharField(max_length=100, verbose_name='Número Interno'),
        ),
        migrations.AlterField(
            model_name='entransito',
            name='observaciones',
            field=models.TextField(blank=True, max_length=400, null=True, verbose_name='Observaciones'),
        ),
        migrations.AlterField(
            model_name='entransito',
            name='operador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='control_app.empleado', verbose_name='Operador'),
        ),
        migrations.AlterField(
            model_name='entransito',
            name='tipo_equipo',
            field=models.CharField(max_length=200, verbose_name='Tipo de Equipo'),
        ),
    ]
