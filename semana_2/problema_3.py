# Oferta "lleve 3 y pague 2"

cantidad = int(input("¿Cuántos productos desea comprar?: "))

while cantidad <= 0:
    cantidad = int(input("Error. Ingrese una cantidad mayor que cero: "))

precios = []

while len(precios) != cantidad:
    entrada = input(f"Ingrese los {cantidad} precios separados por espacios: ")
    precios = [int(precio) for precio in entrada.split()]

    if len(precios) != cantidad:
        print(f"Error. Debe ingresar exactamente {cantidad} precios.")

precios.sort(reverse=True)
total = 0

for i in range(cantidad):
    # En cada grupo de tres, el producto más barato queda gratis.
    if (i + 1) % 3 != 0:
        total += precios[i]

print("El valor mínimo que podría pagar es:", total)
