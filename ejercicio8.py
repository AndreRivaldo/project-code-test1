##Ingresar valores por teclado y determinar todos los valores fraccionarios hasta llegar a dicho número con 5 valores decimales.
input_num = float(input("Ingrese un número: "))

for i in range(1, int(input_num * 100000) + 1):
    fraccion = i / 100000
    if fraccion <= input_num:
        print(f"{fraccion:.5f}")

