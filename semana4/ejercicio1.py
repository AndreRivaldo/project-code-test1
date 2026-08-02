#Escriba función que recibe un texto (varTexto) y un número (varNum) como parámetros
# y muestre por pantalla el texto un número varNum de veces.

def mostrar_texto(varTexto, varNum):
    for _ in range(varNum):
        print(varTexto)

input_text = input("Ingrese un texto: ")
input_num = int(input("Ingrese un número: "))
mostrar_texto(input_text, input_num)