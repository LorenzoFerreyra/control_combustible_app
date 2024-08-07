# Generated by Django 4.1.2 on 2024-06-30 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('res', models.CharField(max_length=255, verbose_name='RES')),
                ('ub_actual', models.CharField(max_length=255, verbose_name='UB-ACTUAL')),
                ('paterno', models.CharField(max_length=255, verbose_name='PATERNO')),
                ('materno', models.CharField(max_length=255, verbose_name='MATERNO')),
                ('nom1', models.CharField(max_length=255, verbose_name='NOM 1')),
                ('nom2', models.CharField(blank=True, max_length=255, null=True, verbose_name='NOM 2')),
                ('cargo', models.CharField(max_length=255, verbose_name='CARGO')),
                ('nivel', models.CharField(max_length=255, verbose_name='NIVEL')),
                ('ingreso', models.DateField(verbose_name='INGRESO')),
                ('salida', models.DateField(blank=True, null=True, verbose_name='SALIDA')),
                ('admin', models.BooleanField(default=False, verbose_name='Admin')),
            ],
            options={
                'verbose_name': 'Empleado',
                'verbose_name_plural': 'Empleados',
            },
        ),
    ]
