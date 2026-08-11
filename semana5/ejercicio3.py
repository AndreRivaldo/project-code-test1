#Determine el valor promedio y la desviación estándar del índice de precios del
#consumidor CPI (inflation_annual_cpi) de los países en toda su historia.

import pandas as pd
from pathlib import Path

carpeta_programa = Path(__file__).parent
ruta_csv = carpeta_programa / "DATA_african_crises.csv"
datos = pd.read_csv(ruta_csv)

# Calcular el promedio y la desviación estándar del índice de precios del consumidor (CPI)
promedio_cpi = datos["inflation_annual_cpi"].mean()
desviacion_estandar_cpi = datos["inflation_annual_cpi"].std()
print(f"El promedio del índice de precios del consumidor (CPI) es: {promedio_cpi}")
print(f"La desviación estándar del índice de precios del consumidor (CPI) es: {desviacion_estandar_cpi}")
