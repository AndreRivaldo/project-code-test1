#Construya un gráfico con la evolución de la variable “exch_usd” en los países que
#no han estado en crisis desde 1960 hasta 2014 considerando el promedio y la
#desviación estándar.

import pandas as pd
import matplotlib.pyplot as plt

# Leer el archivo
from pathlib import Path
#df = pd.read_csv(Path("data", "exch_usd.csv"))
carpeta_programa = Path(__file__).parent
ruta_csv = carpeta_programa / "DATA_african_crises.csv"
datos = pd.read_csv(ruta_csv)

# Filtrar los años entre 1960 y 2014, ambos incluidos
datos_filtrados = datos[
    (datos["year"] >= 1960) &
    (datos["year"] <= 2014) &
    (datos["banking_crisis"] == "no_crisis")
]  

# Calcular el promedio y la desviación estándar por año
resumen = (
    datos_filtrados
    .groupby("year")["exch_usd"]
    .agg(["mean", "std"])
    .reset_index()
)

# Extraer las variables del gráfico
x = resumen["year"]
promedio = resumen["mean"]
desviacion = resumen["std"].fillna(0)   

# Graficar el promedio
plt.figure(figsize=(12, 6))
plt.plot(
    x,
    promedio,
    color="blue",
    label="Promedio de exch_usd (países sin crisis)"
)
# Graficar la desviación estándar como un área
plt.fill_between(
    x,
    promedio - desviacion,
    promedio + desviacion,
    color="lightblue",
    alpha=0.4,
    label="Promedio ± desviación estándar"
)

plt.xlabel("Año")
plt.ylabel("Tipo de cambio (exch_usd)")
plt.title("Evolución de exch_usd en periodos sin crisis")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
