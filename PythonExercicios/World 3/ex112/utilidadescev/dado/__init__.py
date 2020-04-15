def leiaDinheiro(txt):
    while True:
        num = input(txt).replace(',', '.').strip()
        if num.isalpha() or num == '':
            print(f'\033[31mERRO: "{num}" é um preço inválido!\033[m')
        else:
            return float(num)
            break


def leiaInt(txt):
    while True:
        print(txt, end='')
        num = input()
        if not num.isnumeric():
            print('\033[;31mERRO! Digite um número inteiro válido.\033[m')
        else:
            return int(num)
            break
