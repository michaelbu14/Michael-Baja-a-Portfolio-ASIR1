'''Iterables con Loop for'''
# Iterables
# range (número), strings, las listas (arrays unidimensionales), las tuplas (arrays multidimensionales)
# Las listas y tuplas las veremos más adelante

for n in "Administración de Sistema Informáticos en Red":
    print(n)

for caracter in "Administración de Sistemas Informáticos en Red":
    print(caracter)


with open("iterables.txt", "a") as fichero:
    for caracter in "Programación con Python":
        fichero.write(f'{caracter}\n')
