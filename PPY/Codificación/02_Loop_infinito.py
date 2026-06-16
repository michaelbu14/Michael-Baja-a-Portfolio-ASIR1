'''Loop infinito'''

while True:
    mensaje = input(">")
    print("Has escrito", mensaje)
    if mensaje.upper() == "FIN":
        break
    print("A")
