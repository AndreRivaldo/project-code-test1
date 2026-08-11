# Muestre los nombres (sin repetir) de los países que hayan estado en crisis y sean
#independientes con una fecha posterior a 1980

import pandas as pd

# Cargar los datos
#datos = pd.read_csv("DATA_african_crises.csv")
from pathlib import Path


carpeta_programa = Path(__file__).parent
ruta_csv = carpeta_programa / "DATA_african_crises.csv"

datos = pd.read_csv(ruta_csv)

print(datos.head())


# Aplicar las tres condiciones
filtro = (
    (datos["year"] > 1980) &
    (datos["independence"] == 1) &
    (datos["banking_crisis"] == "crisis")
)

# Obtener los nombres sin repetir
paises = datos.loc[filtro, "country"].unique()

print("Países independientes que estuvieron en crisis después de 1980:")
print(paises)