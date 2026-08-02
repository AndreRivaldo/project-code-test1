#Escriba una función en python que reciba 2 arreglos. En caso de que tengan el mismo número de
#elementos, se compare elemento por elemento.
#La función deberá retornar un arreglo de 3 valores. En el índice se indicará el número de 
#elementos del arreglo A que son menores que el arreglo B. En el segundo índice, el número de
#elementos donde ambos son arreglos iguales. En el tercer índice, el número de elementos del 
#arreglo A que son mayores que el arreglo B.

import numpy as np
def comparar_arreglos(array_a, array_b):
    if len(array_a) != len(array_b):
        raise ValueError("Los arreglos deben tener la misma cantidad de elementos.")

    menor = int(np.sum(array_a < array_b))
    igual = int(np.sum(array_a == array_b))
    mayor = int(np.sum(array_a > array_b))

    return [menor, igual, mayor]

arreglos = comparar_arreglos(np.array([1, 2, 3]), np.array([3, 2, 1]))
print(f"Resultado de la comparación: {arreglos}")