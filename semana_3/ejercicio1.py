#Escribe un programa que solicite al usuario un número z, 
#un número de iteraciones numiter por pantalla y calcule la sumatoria

import math

z = float(input("Ingrese un número z: "))
numiter = int(input("Ingrese el número de iteraciones: "))

sumatoria = 0

for k in range(numiter + 1):
    sumatoria += math.pow(z, k) / math.factorial(k)

print("La sumatoria es:", sumatoria)