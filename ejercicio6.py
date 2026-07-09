numero = int(input("ingresa un número:  "))

mayor = numero


while numero != 0:
    if numero > mayor:
        mayor = numero
    numero = int(input("ingresa un número:  "))

print("el mayor numero es: ", mayor)