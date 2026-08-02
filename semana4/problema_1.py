#Escriba el código de la función tipo_triangulo() que recibe como argumentos de entrada
#las longitudes enteras de los 3 lados de un triángulo. La función debe retornar un 0 si el
#triángulo es escaleno, un 1 si es isósceles y un 2 si es equilátero (ver figura 1).

def tipo_triangulo(lado1, lado2, lado3):
    if lado1 == lado2 == lado3:
        return 2  # Equilátero
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        return 1  # Isósceles
    else:
        return 0  # Escaleno
try:
    lado1 = int(input("Ingrese el primer lado: "))
    lado2 = int(input("Ingrese el segundo lado: "))
    lado3 = int(input("Ingrese el tercer lado: "))

    resultado = tipo_triangulo(lado1, lado2, lado3)

    if resultado == 0:
        print("El triángulo es escaleno.")
    elif resultado == 1:
        print("El triángulo es isósceles.")
    else:
        print("El triángulo es equilátero.")

except ValueError:
    print("Error: debe ingresar números enteros.")