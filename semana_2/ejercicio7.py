# Empleando el siguiente diccionario, construya un diccionario de marcas que
# despliegue la cantidad total de apariciones en el diccionario.

centros = {
    "Norte": {"Toyota", "Mazda", "Subaru", "Lexus"},
    "Centro": {"BMW", "Audi", "Lexus", "Skoda"},
}

marcas = {}

for lista_marcas in centros.values():
    for marca in lista_marcas:
        marcas[marca] = marcas.get(marca, 0) + 1

for marca, apariciones in sorted(marcas.items()):
    print(f"Marca: {marca}, apariciones: {apariciones}")
