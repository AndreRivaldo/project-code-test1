import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


# Leer el archivo CSV desde la carpeta del programa
carpeta_programa = Path(__file__).parent
ruta_csv = carpeta_programa / "DATA_athlete_events.csv"

datos = pd.read_csv(ruta_csv)

# Convertir las columnas a valores numéricos
datos["Height"] = pd.to_numeric(datos["Height"], errors="coerce")
datos["Weight"] = pd.to_numeric(datos["Weight"], errors="coerce")
datos["Year"] = pd.to_numeric(datos["Year"], errors="coerce")

# Eliminar filas que no tengan altura, peso o disciplina
datos_validos = datos.dropna(
    subset=["Sport", "Height", "Weight"]
)


# ---------------------------------------------------------
# 1. Relación altura/peso de cada disciplina
# ---------------------------------------------------------

disciplinas = (
    datos_validos.groupby("Sport")[["Height", "Weight"]]
    .mean()
    .reset_index()
)

plt.figure(figsize=(12, 8))

plt.scatter(
    disciplinas["Height"],
    disciplinas["Weight"],
    color="blue",
    alpha=0.7
)

plt.title("Relación entre altura y peso por disciplina")
plt.xlabel("Altura promedio (cm)")
plt.ylabel("Peso promedio (kg)")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()


# ---------------------------------------------------------
# 2. Disciplina con mayor relación altura/peso
# ---------------------------------------------------------

disciplinas["Relacion"] = (
    disciplinas["Height"] / disciplinas["Weight"]
)

indice_mayor = disciplinas["Relacion"].idxmax()
mayor_relacion = disciplinas.loc[indice_mayor]

print("\n2. Disciplina con mayor relación altura/peso:")

print("Disciplina:", mayor_relacion["Sport"])
print(
    "Altura promedio:",
    round(mayor_relacion["Height"], 2),
    "cm"
)
print(
    "Peso promedio:",
    round(mayor_relacion["Weight"], 2),
    "kg"
)
print(
    "Relación:",
    round(mayor_relacion["Relacion"], 4)
)


# ---------------------------------------------------------
# 3. Dispersión altura/peso de Ciclismo por año
# ---------------------------------------------------------

ciclismo = datos_validos[
    datos_validos["Sport"] == "Cycling"
]

ciclismo_por_anio = (
    ciclismo.groupby("Year")[["Height", "Weight"]]
    .mean()
    .reset_index()
    .sort_values("Year")
)

plt.figure(figsize=(12, 8))

grafico = plt.scatter(
    ciclismo_por_anio["Height"],
    ciclismo_por_anio["Weight"],
    c=ciclismo_por_anio["Year"],
    cmap="viridis",
    s=70
)

plt.colorbar(grafico, label="Año")
plt.title("Dispersión de altura y peso en Ciclismo por año")
plt.xlabel("Altura promedio (cm)")
plt.ylabel("Peso promedio (kg)")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()