from interface import *
from arquivo import *
from time import sleep

arq = 'pessoas.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

dados = {}

while True:
    cabeçalho('MENU PRINCIPAL')
    menu()

    try:
        opc = leiaInt('\033[;33mSua opção: \033[m')
    except:
        print('\n\033[;31mDesculpe, algum erro imprevisto aconteceu\033[m')
    else:
        if opc == 1:
            lerArquivo(arq)
        elif opc == 2:
            nome = input('Nome: ')
            idade = leiaInt('Idade: ')
            cadastrar(arq, nome, idade)
        elif opc == 3:
            print('\033[m', end='')
            cabeçalho('Saindo do sistema... Até logo!')
            break
        else:
            print('\n\033[;31mDigite um valor entre 1 e 3.\033[m')
        sleep(1.5)
