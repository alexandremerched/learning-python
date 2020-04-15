def leiaInt(txt):
    while True:
        print(txt, end='')
        num = input()
        if not num.isnumeric():
            print('\033[;31mERRO! Digite um número inteiro válido.\033[m')
        else:
            break 
    return num


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
