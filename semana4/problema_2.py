#Escriba una función que genere el triángulo de Pascal hasta el nivel indicado por el
#usuario (figura 2). La función debe retornar únicamente los valores indicados por el nivel
#indicado. Por ejemplo, si el usuario indica el nivel 9, la función debe retornar un arreglo
#[1,8,28,56,70,56,28,8,1].

def triangulo_pascal(nivel):
    fila = [1]

    for _ in range(1, nivel):
        nueva_fila = [1]

        for i in range(len(fila) - 1):
            nueva_fila.append(fila[i] + fila[i + 1])

        nueva_fila.append(1)
        fila = nueva_fila

    return fila


try:
    nivel = int(input("Ingrese el nivel del triángulo de Pascal: "))

    if nivel < 1:
        print("El nivel debe ser un número entero mayor que cero.")
    else:
        resultado = triangulo_pascal(nivel)
        print(resultado)

except ValueError:
    print("Error: debe ingresar un número entero.")