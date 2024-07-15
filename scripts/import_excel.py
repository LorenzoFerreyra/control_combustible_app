import sys
import os
import django
import pandas as pd

# Añadir el directorio raíz del proyecto al PYTHONPATH
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.append(project_root)

# Configurar la variable de entorno DJANGO_SETTINGS_MODULE
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')

# Inicializar Django
django.setup()

# Importar modelos de Django después de inicializar Django
from control_app.models import Empleado, Equipo, Actividad, Ruta

# Cargar el archivo Excel
df = pd.read_excel(r"C:\Users\Lorenzo\Downloads\Archivo_Import_Renato.xlsx",sheet_name='AUX-ACT')

# Iterar sobre las filas del DataFrame y crear instancias del modelo
for index, row in df.iterrows():
    Actividad.objects.create(
        codigo=row['CODIGO'],
        grupo=row['GRUPO'],
        actividad=row['ACTIVIDAD'],
        subactividad=row['Subactividad'],
        unidad=row['UNIDAD'],
        produccion_diaria_min=row['PRODUCC DIARIA [MIN]'] if pd.notna(row['PRODUCC DIARIA [MIN]']) else 0.0,
        produccion_diaria_max=row['PRODUCC DIARIA [MAX]'] if pd.notna(row['PRODUCC DIARIA [MAX]']) else 0.0,
        produccion_diaria_prom=row['PRODUCC DIARIA [PROM]'] if pd.notna(row['PRODUCC DIARIA [PROM]']) else 0.0,
        produccion_unid_hr_prom=row['PRODUCC UNID/HR [PROM]'] if pd.notna(row['PRODUCC UNID/HR [PROM]']) else 0.0,
        produccion_hr_unid_prom=row['PRODUCC HR/UNID [PROM]'] if pd.notna(row['PRODUCC HR/UNID [PROM]']) else 0.0,
    )
