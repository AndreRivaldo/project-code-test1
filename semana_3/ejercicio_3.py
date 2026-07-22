#Escriba un programa que cree una lista con 10 elementos generados al azar y muestre
#en pantalla el mayor de ellos. Para ello, emplee únicamente listas.

import random

random_numbers = []
for _ in range(10):
    random_numbers.append(random.randint(1, 100))

print("La lista de números aleatorios es:", random_numbers)
print("El mayor de ellos es:", max(random_numbers))