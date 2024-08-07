# Generated by Django 4.1.2 on 2024-06-30 22:40

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('control_app', '0005_remove_ruta_id_alter_ruta_ruta_proyecto_de5_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='proyecto_de5',
            options={'verbose_name': 'Proyecto DE5', 'verbose_name_plural': 'Proyectos DE5'},
        ),
        migrations.RemoveField(
            model_name='empleado',
            name='id',
        ),
        migrations.RemoveField(
            model_name='equipo',
            name='id',
        ),
        migrations.AlterField(
            model_name='empleado',
            name='id_empleado',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='id_item',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='tipo_equipo',
            field=models.CharField(max_length=255, unique=True, verbose_name='TIPO EQUIPO'),
        ),
        migrations.CreateModel(
            name='TransaccionCombustible',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('Ingreso', 'Ingreso'), ('Egreso', 'Egreso')], max_length=20, verbose_name='TIPO')),
                ('subtipo', models.CharField(choices=[('Ingresos propios', 'Ingresos propios'), ('Otros ingresos', 'Otros ingresos'), ('Egresos por transferencia', 'Egresos por transferencia'), ('Ingresos por demasía o remanencia', 'Ingresos por demasía o remanencia')], max_length=50, verbose_name='SUBTIPO')),
                ('fecha', models.DateField(verbose_name='FECHA')),
                ('descripcion', models.CharField(max_length=255, verbose_name='DESCRIPCION')),
                ('gasolina_lt', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='GASOLINA [LT]')),
                ('diesel_lt', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='DIESEL [LT]')),
                ('lubricante_15w40_gasolina', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='15W-40 Gasolina')),
                ('lubricante_15w40_diesel', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='15W-40 Diesel')),
                ('lubricante_aoh68_hidraulico', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='AOH-68 Hidraulico')),
                ('lubricante_85w140', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='85W-140')),
                ('lubricante_80w90', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='80W-90')),
                ('lubricante_mt1_10w_transm', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='MT1-10W TRANSM')),
                ('lubricante_tipo_a', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='TIPO A')),
                ('anticongelante', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='ANTICONGELANTE')),
                ('liquido_frenos', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='LIQUID. FRENOS')),
                ('grasa_rodam', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='RODAM')),
                ('grasa_chasis', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='GRASA CHASIS')),
                ('observaciones', models.CharField(blank=True, max_length=255, null=True, verbose_name='OBSERVACIONES')),
                ('project_link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='control_app.proyecto_de5', verbose_name='Proyecto')),
            ],
            options={
                'verbose_name': 'Transacción de Combustible',
                'verbose_name_plural': 'Transacciones de Combustible',
            },
        ),
        migrations.CreateModel(
            name='EnTransito',
            fields=[
                ('numero', models.AutoField(primary_key=True, serialize=False, verbose_name='Número')),
                ('numero_interno', models.IntegerField(verbose_name='Número Interno')),
                ('gasolina_cargada', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Gasolina Cargada')),
                ('diesel_cargado', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Diesel Cargado')),
                ('lubricante_15w40_gasolina', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='15W-40 Gasolina')),
                ('lubricante_15w40_diesel', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='15W-40 Diesel')),
                ('lubricante_aoh68_hidraulico', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='AOH-68 Hidráulico')),
                ('lubricante_85w140', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='85W-140')),
                ('lubricante_80w90', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='80W-90')),
                ('lubricante_mt1_10w_transm', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='MT1-10W TRANSM')),
                ('fluido_tipo_a', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Fluido Tipo A')),
                ('anticongelante_litros', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Anticongelante Litros')),
                ('liquido_freno', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Líquido de Freno')),
                ('grasa_rodamiento', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Grasa de Rodamiento')),
                ('grasa_chasis', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Grasa de Chasis')),
                ('observaciones', models.TextField(verbose_name='Observaciones')),
                ('operador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='control_app.empleado', verbose_name='Operador')),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='control_app.proyecto_de5', verbose_name='Proyecto')),
                ('tipo_equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='control_app.equipo', to_field='tipo_equipo', verbose_name='Tipo de Equipo')),
            ],
            options={
                'verbose_name': 'En Tránsito',
                'verbose_name_plural': 'Datos en Tránsito',
            },
        ),
    ]
