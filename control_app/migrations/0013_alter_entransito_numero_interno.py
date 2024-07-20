# Generated by Django 4.1.2 on 2024-07-20 02:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('control_app', '0012_entransito_fecha_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entransito',
            name='numero_interno',
            field=models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, to='control_app.equipo', verbose_name='Número Interno'),
        ),
    ]
