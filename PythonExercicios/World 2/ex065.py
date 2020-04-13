total = maior = menor = c = 0

while True:
    on_off = ''

    n = int(input("Digite um número: "))
    on_off = input("Você quer digitar outro número [S/N]: ").upper()
    print(on_off)
    total += n
    c += 1

    if n > maior:
        maior = n
    if n < menor or c == 1:
        menor = n

    while on_off != 'S' and on_off != 'N':
        print("")
        print("Opção inválida.")
        on_off = input("Você quer digitar outro número [S/N]: ").upper()

    if on_off == 'S':
        print("")
    elif on_off == 'N':
        print("""
A média dos números digitados é igual a {}
O maior número é {}
O menor número é {}""".format(total / c, maior, menor))
        break
