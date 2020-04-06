name = input("Digite o seu nome completo: ")

print("""Primeiro nome: {}
Último nome: {}""".format(name.split()[0], name.split()[::-1][0]))
