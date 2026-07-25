#Escriba un programa en Python para un arreglo con las notas de un curso. El programa
#debe calcular el promedio de las notas, extraer la nota menor y mayor. Luego, debe
#mostrar estos tres puntos por pantalla (promedio, nota menor, nota mayor).

import numpy as np

np.random.seed(15)  # Para reproducibilidad
notas = np.random.uniform(1.0, 7.0, size=(30,4)).round(1)  # Genera 10 notas aleatorias entre 1.0 y 7.0  
promedio = np.mean(notas)
nota_menor = np.min(notas)
nota_mayor = np.max(notas)

print(f"Promedio: {promedio}")
print(f"Nota menor: {nota_menor}")
print(f"Nota mayor: {nota_mayor}")