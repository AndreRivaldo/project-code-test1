#Realice la comparación del problema anterior (Ejercicio 3), pero solamente los
#bancos en los momentos de tiempo que NO han estado en crisis. (banking_crisis)

import pandas as pd
from pathlib import Path

carpeta_programa = Path(__file__).parent
ruta_csv = carpeta_programa / "DATA_african_crises.csv"
datos = pd.read_csv(ruta_csv)

# Filtrar los datos para obtener solo los momentos de tiempo que NO han estado en crisis
filtro = datos["banking_crisis"] != "crisis"

grupos = datos[filtro].groupby("country")

grupos[["inflation_annual_cpi"]].agg(["mean", "std"])