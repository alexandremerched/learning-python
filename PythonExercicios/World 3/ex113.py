def leiaInt(txt):
    while True:
        try:
            num = int(input(txt))
        except (ValueError, TypeError):
            print('\033[;31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[;31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return num


def leiaReal(txt):
    while True:
        try:
            num = float(input(txt))
        except (ValueError, TypeError):
            print('\033[;31mERRO: por favor, digite um número real válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[;31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return num

      
num1 = leiaInt('Digite um Inteiro: ')
num2 = leiaReal('Digite um Real: ')
print(f'O valor inteiro digitado foi {num1} e o real foi {num2}')
