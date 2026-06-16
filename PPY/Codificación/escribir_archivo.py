'''Escribir en archivo'''

# Modo 'a' (Append): Añade la línea al final del archivo sin borrar lo que ya estaba escrito.

with open("append.txt", "a") as fichero:
    print("a")
    fichero.write(f'Hola, este es un texto de prueba\n')
    print("a")  # El print sale en la terminal
    fichero.write("Esta es la segunda línea\n")

# with open("escribe.txt", "w") as fichero:
#     print("b")
#     fichero.write("Hola, este es un texto de prueba. \n")
#     print("b")
#     fichero.write("Esta es la segunda linea. \n")


# Modo 'w' (Write): Crea el archivo si no existe o lo sobrescribe si ya existe (borra todo su contenido anterior).
dia = "Jueves"
with open("escribe.txt", "w") as fichero:
    print("b")
    fichero.write(f"La variable {dia} \n")
    print("b")
    fichero.write("Segunda.\n")
