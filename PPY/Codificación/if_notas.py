'''Ejercicio de Notas'''

# nota = float(input("Por favor, dime que nota tienes:"))
# print(nota)
# if nota < 5:
#     print("Has suspendido")
# elif nota < 6:
#     print("Suficiente")
# elif nota < 7:
#     print("Notable")
# elif nota < 9:
#     print("Notable")
# elif nota == 10:
#     print("Matrícula de Honor")
# else:
#     print("Nota no válida")

# Bien hecho:
nota = float(input("Por favor, dime que nota tienes:"))
print(nota)
mensaje = "nada"
if nota > 10:
    mensaje = "Nota fuera de rango"
elif nota == 10:
    mensaje = "MH"
elif nota >= 9:
    mensaje = "Sobresaliente"
elif nota >= 7:
    mensaje = "Notable"
elif nota >= 6:
    mensaje = "Bien"
elif nota >= 5:
    mensaje = "Aprobado"
elif nota >= 0:
    mensaje = "Suspenso"
else:
    mensaje = "No es una nota"  # para números negativos
print(mensaje)
