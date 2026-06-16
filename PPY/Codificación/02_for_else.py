'''Más bucles o Loop for'''

# contraseña = "1234"

# for n in range(3):
#     tucontraseña = input("Introduce la contraseña a ver si aciertas: ")
#     if tucontraseña == contraseña:
#         print("Has acertado")
#         break
# else:
#     print("No has acertado, has agotado todos los intentos")

# # Otra manera
# for n in range(3):
#     print("Intento:", n+1)
#     tucontrasena = input("Introduce la contrasena a ver si aciertas: ")
#     if tucontraseña == contraseña:
#         print("Has acertado: ", contraseña, " en el intento ", n+1)
#         break
# else:
#     print("No has acertado, has agotado todos los intentos")

usuario_correcto = "ASIR"
contraseña_correcta = "1234"

for n in range(3):
    print("Intento:", n + 1)
    tuusuario = input("Introduce el usuario correcto a ver si aciertas: ")
    tucontraseña = input(
        "Introduce la contraseña correcta a ver si aciertas: ")
    if tuusuario == usuario_correcto and tucontraseña == contraseña_correcta:
        print("Has acertado, bienvenido,", tuusuario,
              "Acceso concedido en el intento", n + 1)
        break
else:
    print("No has acertado, has agotado todos los intentos.")
