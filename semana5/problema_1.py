import pandas as pd
from pathlib import Path

carpeta_programa = Path(__file__).parent
ruta_csv = carpeta_programa / "DATA_venta_verduras_y_frutas.csv"

datos = pd.read_csv(ruta_csv)

# Convertir Amount a número, eliminando $, puntos, apóstrofes u otros símbolos.
datos["Amount"] = pd.to_numeric(
    datos["Amount"].astype(str).str.replace(r"[^\d.-]", "", regex=True),
    errors="coerce"
)

# 1. Número de ventas por tipo de fruta y país
frutas = datos[
    datos["Category"].str.strip().str.lower() == "fruit"
]

ventas_frutas_pais = (
    frutas.groupby(["Country", "Product"])
    .size()
    .reset_index(name="Cantidad")
)

print("\n1. Número de frutas vendidas por tipo y país:")
print(ventas_frutas_pais.to_string(index=False))


# 2. Fruta con el mayor monto total de ventas
ventas_totales = (
    frutas.groupby("Product")["Amount"]
    .sum()
    .sort_values(ascending=False)
)

fruta_mayor_venta = ventas_totales.idxmax()
monto_mayor_venta = ventas_totales.max()

print("\n2. Fruta con mayor venta total:")
print(fruta_mayor_venta, "-", monto_mayor_venta)


# 3. Monto promedio de ventas de cada fruta
promedio_por_fruta = (
    frutas.groupby("Product")["Amount"]
    .mean()
    .sort_values(ascending=False)
)

print("\n3. Monto promedio de ventas de cada fruta:")
print(promedio_por_fruta)


# 4. País que compra la mayor cantidad de zanahorias
zanahorias = datos[
    datos["Product"].str.strip().str.lower() == "carrots"
]

zanahorias_por_pais = zanahorias.groupby("Country").size()
pais_mas_zanahorias = zanahorias_por_pais.idxmax()
cantidad_zanahorias = zanahorias_por_pais.max()

print("\n4. País que compra la mayor cantidad de zanahorias:")
print(pais_mas_zanahorias, "-", cantidad_zanahorias, "ventas")