import math


x = []
y = []

print("Ingrese las 10 coordenadas de X:")
for i in range(10):
    valor = float(input(f"X[{i}]: "))
    x.append(valor)

print("\nIngrese las 10 coordenadas de Y:")
for i in range(10):
    valor = float(input(f"Y[{i}]: "))
    y.append(valor)

print("\nPuntos más cercanos:")

for i in range(10):
    distancia_minima = None
    indice_cercano = -1

    for j in range(10):
        if i != j:
            diferencia_x = x[i] - x[j]
            diferencia_y = y[i] - y[j]
            distancia = math.sqrt(diferencia_x**2 + diferencia_y**2)

            if distancia_minima is None or distancia < distancia_minima:
                distancia_minima = distancia
                indice_cercano = j

    print(
        f"({x[i]:g}, {y[i]:g}) -> "
        f"({x[indice_cercano]:g}, {y[indice_cercano]:g}), "
        f"distancia: {distancia_minima:.2f}"
    )
