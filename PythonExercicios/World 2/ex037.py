num = int(input("Digite o número para ser convertido: "))

option = int(input("""Digite 1 para Binário.
Digite 2 para Octal.
Digite 3 para Hexadecimal.

"""))

if option == 1:
    print("O número em binário é igual a {}".format(bin(num)[2:]))
elif option == 2:
    print("O número em octal é igual a {}".format(oct(num)[2:]))
elif option == 3:
    print("O número em hexadecimal é igual a {}".format(hex(num)[2:]))
else:
    print("Opção inválida.")