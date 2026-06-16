'''Importando el módulo Math'''
# Importar una líbrería
import math

print("Probando math.ceil()")
# Ceil va al número entero más cercano
# math.ceil() redondea al número entero más cercano por arriba
print(math.ceil(3.43))
print(math.ceil(-3.43))

a = 5
b = 2
print(a/b)
print(math.ceil(a/b))

print(-a/b)
print(math.ceil(-a/b))

a = 9
b = 2
print(a/b)
print(math.ceil(a/b))

# math.floor() redondea al número entero más cercano por abajo
print("Probando math floor()")
print(math.floor(3.99))
print(math.floor(-3.99))

# math.isnan() "isnan" significa "no es un número" por tanto devuelve false si es número
print(math.isnan(56.24))
# print(math.isnan("56.24")) #ERROR

# math.pow (base, exponente) es hacer potencias
print(math.pow(2, 8))

# math.sqrt () raíz cuadrada
print(math.sqrt(144))
