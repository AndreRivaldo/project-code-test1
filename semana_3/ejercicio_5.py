#Un científico extranjero estaba haciendo estudios de la altura de las personas en
#nuestro país y guardó sus datos en un arreglo NumPy llamado alturas. Sin embargo,
#utilizó pulgadas como medida. Escriba el código para transformar esas mediciones
#a centímetros. Considere que los datos de la lista son ingresados manualmente.

import numpy as np

input_data = input("Ingrese las alturas en pulgadas separadas por comas: ")
# Convertir la cadena de entrada en una lista de números flotantes

alturas = np.array([float(x.strip()) for x in input_data.split(',')])  # Alturas en pulgadas
alturas_cm = alturas * 2.54  # Convertir a centímetros
print("Alturas en pulgadas:", alturas)
print("Alturas en centímetros:", alturas_cm)