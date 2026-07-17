#Empleando el siguiente diccionario, busque el tipo de música más antiguo

dcc_clasica = {
    "Autor":"Vivaldi","Composicion":"Las cuatro estaciones","Año":1723
    }
dcc_jazz = {
    "Autor":"Pat Metheny","Composicion":"Last train Home","Año":1987
    }
dcc_pop = {
    "Autor":"Madonna","Composicion":"Material girl","Año":1984
    }
musica = {
    "Clasica":dcc_clasica,
 "Jazz":dcc_jazz,
 "Pop":dcc_pop
}

for tipo_musica, datos in musica.items():
    print("Tipo de música:", tipo_musica)
    print("Autor:", datos["Autor"])
    print("Composición:", datos["Composicion"])
    print("Año:", datos["Año"])
    print()
# Encontrar el tipo de música más antiguo

for tipo_musica, datos in musica.items():
    if datos["Año"] == min(musica[tipo]["Año"] for tipo in musica):
        print("El tipo de música más antiguo es:", tipo_musica)
        print("Autor:", datos["Autor"])
        print("Composición:", datos["Composicion"])
        print("Año:", datos["Año"])
        break
    