import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Conexión a la base de datos 'datos_mison.db'
conexion = sqlite3.connect('datos_mision.db')

# Extracción de datos con SQL
consulta = "SELECT * FROM tabla_exoplanetas;"
df = pd.read_sql_query(consulta, conexion)
conexion.close()

print("Datos extraídos de la Base de Datos:")
print(df)

# Cálculos para determinar cuáles planetas son rocosos y cuáles gaseosos
df["densidad"] = df["pl_bmasse"] / (df["pl_rade"]**3)
df["densidad_gcm3"] = df["densidad"] * 5.51

def clasificar_planeta(fila):
    if fila["pl_rade"] < 1.8 and fila["densidad_gcm3"] > 3:
        return "rocoso"
    elif fila["pl_rade"] > 4:
        return "gigante_gaseoso"
    else:
        return "intermedio"

df["tipo"] = df.apply(clasificar_planeta, axis=1)

# Generar la gráfica masa vs radio: 'resultado.png'
plt.figure(figsize=(8,6))

for t in df["tipo"].unique():
    sub = df[df["tipo"] == t]
    plt.scatter(sub["pl_rade"], sub["pl_bmasse"], label=t, alpha=0.6)

plt.axvline(1.8, linestyle="--", label="Transición rocoso-gaseoso")
plt.axvline(4, linestyle=":", color="black", label="Inicio régimen gigantes gaseosos")
plt.xscale("log")
plt.yscale("log")
plt.title('Masa vs Radio Exoplanetas')
plt.xlabel('Radio (Radios Terrestres)')
plt.ylabel('Masa (Masas Terrestres)')
plt.legend()
plt.tight_layout()
plt.savefig('resultado.png')
