value = int(input("""Digite 1 para Binário.
Digite 2 para Octal.
Digite 3 para Hexadecimal.

"""))

num = int(input("Digite o número para ser convertido: "))

if 1:
    print("O número em binário é igual a {}".format(int("2", 10)))
elif 2:
    print("O número em octal é igual a {}".format(oct(value)))
elif 3:
    print("O número em hexadecimal é igual a {}".format(hex(value)))