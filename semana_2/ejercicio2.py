#Dada una lista con números enteros, calcule cuántos números pares hay en la lista.

numeros = []

input_count = int(input("Ingrese la cantidad de números que desea ingresar: "))

for i in range(input_count):
    numero = int(input("Ingrese un número entero: "))
    numeros.append(numero)

pares = 0

for numero in numeros:
    if numero % 2 == 0:
        pares += 1

print("La cantidad de números pares es:", pares)
