'''Operador ternario 03'''

import random
numero_aleatorio = random.randint(0, 10)
print(numero_aleatorio)
numero2 = int(input("Introduce un número, a ver si lo adivinas:"))

mensaje = "Has acertado" if numero2 == numero_aleatorio else "Prueba otra vez"

print(mensaje)
