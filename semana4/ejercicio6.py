#Escriba una función en Python que permita ingresar un conjunto de datos por teclado
#separados por coma. Los datos pueden ser cualquier número (entero o flotante),
#inclusive el cero. Luego, debe dividir la suma por el total de números ingresados.
#En caso que el usuario no ingrese un número, su programa debe indicar que no
#ha ingresado números. Si el usuario ingresa un carácter en vez de un número, su
#programa debe reemplazar el carácter por un cero.

def calcular_promedio():
    datos = input("Ingrese datos separados por coma: ").strip()

    if not datos:
        print("No ha ingresado números.")
        return None

    lista_datos = datos.split(",")
    suma = 0

    for dato in lista_datos:
        try:
            suma += float(dato.strip())
        except ValueError:
            print(f"'{dato}' no es un número válido. Se reemplazará por 0.")
            # No se suma nada porque el carácter se considera cero.

    return suma / len(lista_datos)


promedio = calcular_promedio()

if promedio is not None:
    print(f"El promedio de los datos ingresados es: {promedio}")