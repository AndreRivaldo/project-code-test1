#Escriba un programa en Python que: solicite al usuario num (un número entero),
#genere una matriz cuadrada de tamaño num con la tabla de multiplicar y la muestre
#por pantalla.

import numpy as np

num = int(input("Ingrese un número entero para el tamaño de la matriz: "))
tabla_multiplicar = np.zeros((num, num), dtype=int) 

for i in range(num):
    for j in range(num):
        tabla_multiplicar[i, j] = (i + 1) * (j + 1)

print("Tabla de multiplicar:")
print(tabla_multiplicar)