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
df = pd.read_excel(r"C:\Users\Lorenzo\Downloads\Archivo_Import_Renato.xlsx")

# Iterar sobre las filas del DataFrame y crear instancias del modelo
for index, row in df.iterrows():
    Equipo.objects.create(
        paterno=row['PATERNO'],
        materno=row['MATERNO'],
        nom1=row['NOM 1'],
        nom2=row['NOM 2'],
        cargo=row['CARGO'],
    )
