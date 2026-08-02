#Escriba una función anónima (lambda) en Python que, dada una lista, determine el
#promedio de los valores superiores o iguales a 5.
#No utilice una función de NumPy, únicamente filter y anónima.

def promedio_superiores_a_cinco(lista):
    # Filtrar los valores superiores o iguales a 5
    valores_filtrados = list(filter(lambda x: x >= 5, lista))
    
    # Calcular el promedio si hay valores filtrados
    if valores_filtrados:
        promedio = sum(valores_filtrados) / len(valores_filtrados)
        return promedio
    else:
        return None  # Retornar None si no hay valores superiores o iguales a 5


try:
    entrada = input("Ingrese los valores separados por espacios o comas: ")
    valores = [float(valor) for valor in entrada.replace(",", " ").split()]

    if not valores:
        print("Error: debe ingresar al menos un valor.")
    else:
        promedio = promedio_superiores_a_cinco(valores)
        if promedio is None:
            print("No hay valores superiores o iguales a 5.")
        else:
            print(f"El promedio de los valores superiores o iguales a 5 es: {promedio}")
except ValueError:
    print("Error: ingrese solamente valores numéricos.")
