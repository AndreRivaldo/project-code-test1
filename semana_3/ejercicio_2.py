#Escriba un programa que muestre por pantalla la multiplicación entre dos números
#en forma aleatoria y le pida al usuario resolverla (números entre 1 y 10).
#Si el usuario se demoró más de 10 segundos en resolverla, debe desplegar el mensaje
#“eres muy lento, el resultado era X” (donde X corresponda al resultado real). En caso
#contrario, verifique si el usuario pudo resolver la multiplicación en forma correcta,
#felicitándolo, o bien mostrando la solución de la multiplicación. 

import random
import time


numero_1 = random.randint(1, 10)
numero_2 = random.randint(1, 10)
resultado_real = numero_1 * numero_2

inicio = time.time()
respuesta = int(input(f"¿Cuánto es {numero_1} x {numero_2}? "))
fin = time.time()

tiempo_transcurrido = fin - inicio

if tiempo_transcurrido > 5:
    print(f"Eres muy lento, el resultado era {resultado_real}")
elif respuesta == resultado_real:
    print("¡Felicitaciones! Respuesta correcta.")
else:
    print(f"Respuesta incorrecta. El resultado era {resultado_real}")
