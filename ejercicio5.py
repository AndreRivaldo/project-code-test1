numero = int(input("ingresa un número:  "))

contador = 0
suma = 0

while numero != 0:
    contador = contador + 1
    suma = suma + numero
    numero = int(input("ingresa un número:  "))
print("ingresaste:", contador , "numeros que suma", suma )