##(La formula que debe programarse es: sin(x) = Σ (-1)^i * x^(2i+1) / (2i+1)!

#termino = (-1)**i * (x_rad ** (2*i + 1)) / math.factorial(2*i + 1)

import math

x = input("Ingrese x en grados entre 0 y 360: ")

while not x.isdigit() or int(x) < 0 or int(x) > 360:
    x = input("Error. Ingrese x entero entre 0 y 360: ")

x = int(x)
x_rad = math.radians(x)

n = input("Ingrese la cantidad de iteraciones n: ")

while not n.isdigit():
    n = input("Error. Ingrese n entero: ")

n = int(n)

seno = 0
i = 0

while i <= n:
    termino = ((-1) ** i) * (x_rad ** (2 * i + 1)) / math.factorial(2 * i + 1)
    seno = seno + termino
    i = i + 1

print("El seno aproximado es:", seno)
print("El seno real es:", math.sin(x_rad))