#Escriba una función en python que reciba 2 arreglos. En caso que ambos arreglos
#tenga la misa cantidad de dimensiones, calcule la distancia entre los puntos, en caso
#contrario, devuelva "-1"

import numpy as np

def calcular_distancia(punto1, punto2):
    if len(punto1) != len(punto2):
        return "-1"
    return np.linalg.norm(np.array(punto1) - np.array(punto2))
##Ejemplo 1 (ALEATORIO)
#random_point1 = np.random.rand(3)  # Genera un punto aleatorio en 3D
#random_point2 = np.random.rand(3)  # Genera otro punto aleatorio en 3D
#distancia = calcular_distancia(random_point1, random_point2)
#if distancia == "-1":
    #print("Los puntos no tienen la misma cantidad de dimensiones.")
#else:
    #print(f"La distancia entre los puntos {random_point1} y {random_point2} es: {distancia}")
    #EJEMPLO 2 (INGRESO POR TECLADO)
input_point1 = input("Ingrese el primer punto (separado por comas): ")
input_point2 = input("Ingrese el segundo punto (separado por comas): ")
punto1 = [float(x) for x in input_point1.split(",")]
punto2 = [float(x) for x in input_point2.split(",")]
distancia = calcular_distancia(punto1, punto2)
if distancia == "-1":
        print("-1.")
else:
    print(f"La distancia entre los puntos {punto1} y {punto2} es: {distancia}")

#Puedo usar arrays de numpy para ingresar los puntos.