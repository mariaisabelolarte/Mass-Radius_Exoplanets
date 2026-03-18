import sqlite3
import pandas as pd

# Lectura del csv con pandas
df = pd.read_csv('datos_exoplanetas.csv')

# Filtrado de datos
df = df.dropna(subset=['pl_rade', 'pl_bmasse'])
df = df[df["pl_rade"] > 0]
df = df[df["pl_bmasse"] > 0]

print(f"Planetas guardados: {len(df)}")

# Conexion a la base de datos
conexion = sqlite3.connect('datos_mision.db')

# Guardado del df como tabla SQL
df.to_sql('tabla_exoplanetas', conexion, if_exists='replace', index=False)
conexion.close()
