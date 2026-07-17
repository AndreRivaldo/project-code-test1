#Genere una lista con 10 números enteros ingresados por el usuario y muestre los
#valores en forma ordenada

numeros = []

for i in range(10):
    numero = int(input("Ingrese un número entero: "))
    numeros.append(numero)

numeros.sort()

print("Los valores en forma ordenada son:", numeros)