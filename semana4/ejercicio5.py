#Imagínese que, en un arreglo de tamaño num, hay una mosca en la posición pos. La
#mosca se mueve de forma aleatoria (al azar) a la izquierda, a la derecha o se queda
#quieta. En caso que la mosca se salga del arreglo, la mosca es atrapada por una araña.
#Para modelar el comportamiento de la mosca, usted debe generar un número
#aleatorio entre 0 y 1. Si el número es menor a 0.33, entonces la mosca se mueve a
#la izquierda. En caso que sea un número entre 0.33 y 0.66, se mantiene quieta. Si es
#mayor a 0.66, se mueve a la derecha.
#Cree una función que reciba dos parámetros: num y pos y luego itere hasta que la
#mosca sea atrapada por alguna araña. Luego, muestre por pantalla el número de veces
#que la mosca estuvo en cada posición y el número total de movimientos realizados.

import random
import numpy as np


def simular_mosca(num, pos):
    if num <= 0:
        raise ValueError("El tamaño del arreglo debe ser mayor que cero.")
    if pos < 0 or pos >= num:
        raise ValueError("La posición inicial de la mosca debe estar dentro del arreglo.")

    posiciones = np.zeros(num, dtype=int)
    movimientos = 0
    posicion_actual = pos

    while 0 <= posicion_actual < num:
        posiciones[posicion_actual] += 1
        movimientos += 1

        movimiento = random.random()
        if movimiento < 0.33:
            posicion_actual -= 1
        elif movimiento > 0.66:
            posicion_actual += 1

    return posiciones, movimientos


num = 10
pos = 5
posiciones, movimientos = simular_mosca(num, pos)
print(f"Posiciones visitadas: {posiciones}")
print(f"Número total de movimientos: {movimientos}")

