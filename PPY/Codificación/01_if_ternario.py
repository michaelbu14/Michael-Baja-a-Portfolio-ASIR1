'''Operador ternario 01'''

edad = 15
print(edad)
if edad >= 18:
    mensaje = "Mayor de edad con if clásico"
else:
    mensaje = "Es menor de edad con if clásico"
print(mensaje)

# Con el operador ternario se aumenta la eficacia del código
# Se llama ternario porque tiene 3 partes

edad = int(input("Introduce la edad:"))

mensaje = "Mayor de edad con if ternario" if edad >= 18 else "Es menor de edad con if ternario"

print(mensaje)
