#Escriba una función que convierta una lista con números a una cadena donde todos
#los números se unan mediante la función reduce.

from functools import reduce


def convertir_lista_a_cadena(lista):
    return reduce(
        lambda acumulado, numero: acumulado + str(numero),
        lista,
        ""
    )


try:
    entrada = input("Ingrese números separados por espacios o comas: ")

    lista = [
        float(numero)
        for numero in entrada.replace(",", " ").split()
    ]

    if not lista:
        print("Debe ingresar al menos un número.")
    else:
        cadena = convertir_lista_a_cadena(lista)
        print(f"Cadena resultante: {cadena}")

except ValueError:
    print("Error: debe ingresar solamente números.")