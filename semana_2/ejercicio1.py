# Llene una lista con números enteros y calcule la suma de ellos.
# La lista debe ser creada manualmente con distintos números y cantidad de elementos.
# #Me faltó agregar los datos por teclado.

numeros = []
for i in range(5):
    numero = int(input("Ingrese un número entero: "))
    numeros.append(numero)

suma = 0

for numero in numeros:
    suma += numero

print("Lista de números:", numeros)
print("La suma de los números es:", suma)
