def py_help():
    from time import sleep

    while True:
        sleep(1)
        título = 'SISTEMA DE AJUDA PyHELP'
        print('\033[32m', end='')
        print('~'*(len(título)+4))
        print(f'  {título}  ')
        print('~'*(len(título)+4), end='\033[m\n')

        opc = input('Função ou Biblíoteca > ').lower()

        if opc == 'fim':
            break 

        sleep(1)
        acessando = f"Acessando o manual do comando '{opc}'"
        print('\033[34m', end='')
        print('~'*(len(acessando)+4))
        print(f'  {acessando}  ')
        print('~'*(len(acessando)+4), end='\033[m\n')

        print('\033[35m')
        sleep(1)
        help(opc)
        print('\033[m', end='')
        
    fim = 'ATÉ LOGO!'
    print('\033[31m', end='')
    print('~'*(len(fim)+4))
    print(f'  {fim}  ')
    print('~'*(len(fim)+4), end='\033[m\n')


py_help()
