#Dada una lista con números enteros, encuentre el menor número de la lista.

numeros = [3, 7, 1, 9, 4, 2]
menor = numeros[0]

for numero in numeros:
    if numero < menor:
        menor = numero

print("El menor número de la lista es:", menor)
print("La lista de números es:", numeros)
