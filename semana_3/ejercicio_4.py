#Realice un programa que cree un arreglo con 10 elementos generados al azar y
#muestre en pantalla el mayor de ellos, con la biblioteca NumPy.

try:
	import numpy as np
	use_numpy = True
except Exception:
	import random
	use_numpy = False

if use_numpy:
	random_array = np.random.randint(1, 101, size=10)
	max_value = np.max(random_array)
else:
	random_array = [random.randint(1, 100) for _ in range(10)]
	max_value = max(random_array)

print("El arreglo de números aleatorios es:", random_array)
print("El mayor de ellos es:", max_value)