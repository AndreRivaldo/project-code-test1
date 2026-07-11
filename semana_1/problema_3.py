secuencia = input("Ingrese una secuencia de ADN de hasta 100 caracteres: ").upper()

while (
    len(secuencia) > 100
    or len(secuencia) == 0
    or any(letra not in "ATCG" for letra in secuencia)
):
    secuencia = input(
        "Error. Ingrese entre 1 y 100 caracteres usando solo A, T, C o G: "
    ).upper()

cantidad = 0

for i in range(len(secuencia) - 3):
    if secuencia[i] == "A" and secuencia[i + 2] == "T":
        cantidad += 1

print(cantidad, "secuencias detectadas")
