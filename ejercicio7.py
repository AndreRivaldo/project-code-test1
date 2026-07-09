##Divisores de un número
##Divisores de un número
numero = int(input("Ingresa un número para conocer sus divisores:  "))
divisores = []

for i in range(1, numero + 1):
    if numero % i == 0:
        divisores.append(i)

print("Los divisores de", numero, "son:", divisores)
