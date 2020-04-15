def cabeçalho(txt):
    print('-' * 40)
    print(f'{txt:^40}')
    print('-' * 40)


def menu():
    print('-'*40)
    print('\033[;33m1\033[m - \033[;36mVer pessoas cadastradas\033[m')
    print('\033[;33m2\033[m - \033[;36mCadastrar nova Pessoa\033[m')
    print('\033[;33m3\033[m - \033[;36mSair do Sistema\033[m')
    print('-'*40)


def leiaInt(txt):
    while True:
        try:
            num = int(input(txt))
        except (ValueError, TypeError):
            print(
                '\033[;31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[;31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        except:
            print('\n\033[;31mDesculpe, algum erro imprevisto aconteceu\033[m')
        else:
            return num
