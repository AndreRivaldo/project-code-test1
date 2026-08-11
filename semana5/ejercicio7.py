#Construya un gráfico del tipo histograma de la variable “‘exch_usd” desde 1860 hasta
#2014 de todos los países.

import pandas as pd
import matplotlib.pyplot as plt

# Leer el archivo
from pathlib import Path
carpeta_programa = Path(__file__).parent
ruta_csv = carpeta_programa / "DATA_african_crises.csv"
datos = pd.read_csv(ruta_csv)

# Filtrar los años entre 1860 y 2014, ambos incluidos
datos_filtrados = datos[
    (datos["year"] >= 1860) &
    (datos["year"] <= 2014)
]   

# Graficar el histograma
plt.figure(figsize=(12, 6))
plt.hist(
    datos_filtrados["exch_usd"].dropna(),
    bins=30,
    color="blue",
    alpha=0.7,
    edgecolor="black"
)
plt.title("Histograma de exch_usd entre 1860 y 2014")
plt.xlabel("exch_usd")
plt.ylabel("Frecuencia")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()  