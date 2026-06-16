'''Variables de tipo String'''
sigla_formativo = "ASIR"
nivel_educativo = 'Formación Profesional'  # Puede ser comillas simple también
# Para string largos que ocupan varias líneas usamos las triple dobles comillas.
ciclo_formativo = """Ciclo Formativo de Grado Superior Administración de Sistemas Informáticos
en Red de la familia de Informática"""

print(sigla_formativo, nivel_educativo, ciclo_formativo)

long1 = len(sigla_formativo)
# Len(argumento) los argumentos son los valores que le pasamos a una función
print(long1)

print(len(sigla_formativo))

print(len("Pedro Guerrero López"))

c1 = nivel_educativo[0]
print(c1)

print(nivel_educativo[1])

print(ciclo_formativo[0:15])

print(ciclo_formativo[19:33])

print(ciclo_formativo[34:])

print(ciclo_formativo[:81])

print(ciclo_formativo[:])
