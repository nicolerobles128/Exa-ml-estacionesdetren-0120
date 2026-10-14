import sys
import os
import io
import pandas as pd
import importlib.util

# 1. Ruta exacta al archivo dicc-0120.py (con guión medio)
ruta_dicc = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "datos-de-entrada-ml-0120", "dicc-0120.py")
)

# 2. Cargar el módulo de forma dinámica
spec = importlib.util.spec_from_file_location("dicc_0120", ruta_dicc)
if spec is None or spec.loader is None:
    raise ImportError(f"No se pudo encontrar el archivo en: {ruta_dicc}")

dicc_0120 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dicc_0120)

print("Nicole Robles Machine Learning pandas, NC 0120")

# Variable para almacenar las salidas y guardarlas en el archivo .md
contenido_md = []
encabezado_pie = "Nicole Robles Machine Learning pandas, NC 0120"
contenido_md.append(f"# Reporte de Análisis de Datos - Pandas\n\n`{encabezado_pie}`\n")

def registrar(titulo, contenido):
    """Muestra el resultado en terminal y lo formatea para el archivo Markdown."""
    print(f"\n--- {titulo} ---")
    print(contenido)
    contenido_md.append(f"## {titulo}\n```text\n{contenido}\n```\n")

# 1. Convertir diccionario a DataFrame
df = pd.DataFrame(dicc_0120.datos_estaciones)
registrar("1. DataFrame Convertido", df)

# 2. Información Estructural
registrar("2.1 Primeras Filas (head)", df.head(2))
registrar("2.2 Últimas Filas (tail)", df.tail(2))
registrar("2.3 Dimensiones (Filas, Columnas)", df.shape)
registrar("2.4 Tipos de Datos por Columna", df.dtypes)

# Capturar salida de df.info()
buffer = io.StringIO()
df.info(buf=buffer)
registrar("2.5 Información General (info)", buffer.getvalue())

# 3. Estadísticas Generales de una Columna Numérica (Pasajeros_dia)
registrar("3. Estadísticas Generales de la Columna 'Pasajeros_dia'", df['Pasajeros_dia'].describe())

# 4. Ordenar Ascendente por Pasajeros_dia
df_asc_pasajeros = df.sort_values(by="Pasajeros_dia", ascending=True)
registrar("4. Ordenar Ascendente por Pasajeros_dia", df_asc_pasajeros)

# 5. Ordenar Descendente por Trenes_dia
df_desc_trenes = df.sort_values(by="Trenes_dia", ascending=False)
registrar("5. Ordenar Descendente por Trenes_dia", df_desc_trenes)

# 7. Guardar el archivo resultados-ml-0120.md dentro de resultados-0120
carpeta_resultados = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'resultados-0120'))
os.makedirs(carpeta_resultados, exist_ok=True)
ruta_archivo_md = os.path.join(carpeta_resultados, "resultados-ml-0120.md")

contenido_md.append(f"`{encabezado_pie}`")

with open(ruta_archivo_md, "w", encoding="utf-8") as f:
    f.write("\n".join(contenido_md))

print(f"\n[ÉXITO] Archivo generado correctamente en: {ruta_archivo_md}")
print("Nicole Robles Machine Learning pandas, NC 0120")