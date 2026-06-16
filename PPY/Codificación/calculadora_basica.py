'''Calculadora básica'''
# input() toma lo que recoge del usuario como string
a1 = input("Inroduce el primer número:")
a2 = input("Inroduce el segundo número:")
a = a1+a2
print(a)

# Solucionamos
a1 = input("Inroduce el primer número:")
a1 = int(a1)

# Otra manera
a2 = int(input("Inroduce el segundo número:"))

a = a1+a2
print(a)
################################################
a1 = int(input("Inroduce el primer número:"))
a2 = int(input("Inroduce el segundo número:"))
suma = a1+a2
resta = a1-a2
multiplicacion = a1*a2
division = a1/a2

mensaje1 = f"Con los numeros introducidos {a1} y {a2}, la suma es {suma}, la resta es {resta}, la multiplicacion es {multiplicacion} y la división es {division}"
print(mensaje1)

# print(suma)
# print(resta)
# print(multiplicacion)
# print(division)

# Para permitir enter """
mensaje2 = f"""
Con los numeros introducidos {a1} y {a2}, 
la suma es {suma}, 
la resta es {resta}, 
la multiplicacion es {multiplicacion} 
y la división es {division}"""
print(mensaje2)
