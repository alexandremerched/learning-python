while True:
    n1 = int(input("Digite o 1° número: "))
    n2 = int(input("Digite o 2° número: "))

    option = int(input("""
O que você quer fazer com esses valores:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa

"""))

    if option == 1:
        print("A soma de {} e {} é igual a {}".format(n1, n2, n1 + n2))
    elif option == 2:
        print("O produto de {} e {} é igual a {}".format(n1, n2, n1 * n2))
    elif option == 3:
        if n1 >= n2:
            print("O maior número é".format(n1))
        elif n1 < n2:
            print("O maior número é".format(n2))
    elif option == 5:
        break

    print("")