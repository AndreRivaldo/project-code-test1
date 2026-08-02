#Escriba una función que determine los números primos hasta un determinado valor
#ingresado por el usuario.

def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def encontrar_primos(limite):
    primos = []
    for n in range(2, limite + 1):
        if es_primo(n):
            primos.append(n)
    return primos

limit = int(input("Ingrese un número: "))
print("Números primos hasta", limit, ":", encontrar_primos(limit))