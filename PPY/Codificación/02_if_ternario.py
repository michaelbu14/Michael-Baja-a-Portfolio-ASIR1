'''Operador ternario 02'''

numero1 = 8
numero2 = int(input("Introduce un número, a ver si lo adivinas:"))

mensaje = "Has acertado" if numero2 == numero1 else "Prueba otra vez"

print(mensaje)
