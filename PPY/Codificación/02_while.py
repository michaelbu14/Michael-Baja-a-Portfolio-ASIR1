'''Loop while'''

comando = ""  # string vacío
while comando != "FIN":
    comando = input("$")
    print("Has escrito", comando)

comando = ""  # string vacío
while comando.upper() != "FIN":
    comando = input(">")
    print("Has escrito", comando)
