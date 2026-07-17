#Construya una estructura de diccionario con los nombres de países y capitales de
#Sudamérica y luego despliegue por pantalla el nombre del país.

paises_capitales = {
    "Brasil": "Brasilia",
    "Argentina": "Buenos Aires",
    "Colombia": "Bogota",
    "Venezuela": "Caracas",
    "Peru": "Lima",
    "Chile": "Santiago",
    "Ecuador": "Quito",
    "Bolivia": "La Paz",
    "Paraguay": "Asuncion",
    "Uruguay": "Montevideo"
}

for pais in paises_capitales:
    print("El nombre del país es:", pais)
    print("La capital es:", paises_capitales[pais])
