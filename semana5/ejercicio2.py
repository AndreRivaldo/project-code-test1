#Muestre el país del continente africano con el mayor número de crisis en la historia.
#Utilice la siguiente columna para conocer si tuvo o no crisis.
#banking_crisis (valores: ‘crisis’ o ‘no_crisis’)

import pandas as pd
from pathlib import Path

carpeta_programa = Path(__file__).parent
ruta_csv = carpeta_programa / "DATA_african_crises.csv"
datos = pd.read_csv(ruta_csv)

# Contar el número de crisis por país
conteo_crisis = datos[datos["banking_crisis"] == "crisis"].groupby("country").size()
pais_con_mas_crisis = conteo_crisis.idxmax()
print(f"El país con el mayor número de crisis es: {pais_con_mas_crisis}")