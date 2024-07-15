# scripts/import_excel.py
import pandas as pd
from control_app.models import Empleado, Equipo, Actividad, Ruta
import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()


df = pd.read_excel("C:\Users\Lorenzo\Downloads\Archivo_Import_Renato.xlsx")


for index, row in df.iterrows():
    Empleado.objects.create(
        paterno=row['PATERNO'],
        materno=row['MATERNO'],
        nom1=row['NOM 1'],
        nom2=row['NOM 2'],
        cargo=row['CARGO'],
        
    )
