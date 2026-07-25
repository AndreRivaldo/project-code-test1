#Cree un código que genere una matriz de 40x3 que represente las notas tanto de
#controles como de la primera y segunda prueba de los estudiantes de un curso. Llene
#esta matriz con números aleatorios entre 1 y 7. Finalmente, cree una nueva matriz
#unidimensional de tamaño 40, con los promedios simples de cada estudiante y
#muéstrela por pantalla.

import numpy as np

np.random.seed(15)  # Para reproducibilidad
notas = np.random.uniform(1.0, 7.0, size=(40, 3)).round(1)  # Genera 40x3 notas aleatorias entre 1.0 y 7.0
promedios = np.mean(notas, axis=1).round(1) [:,np.newaxis]  # Calcula el promedio de cada estudiante

notas_finales= np.hstack((notas, promedios))  # Combina las notas con los promedios en una nueva matriz
print("Matriz de notas y promedios:\n", notas_finales)  
#print("Matriz de notas:\n", notas)
#print("Promedios de cada estudiante:\n", promedios)