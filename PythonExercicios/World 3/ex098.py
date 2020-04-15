from time import sleep


def contador(i, f, p, v=0.5):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :param v: velocidade da contagem em segundos
    :return: sem retorno
    Funcao criada por Alexandre Merched
    """

    if p < 0:
        p *= (-1)
    elif p == 0:
        p = 1

    print('-=' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2)

    if i < f:
        while i <= f:
            print(i, end=' ', flush=True)
            sleep(v)
            i += p
    elif f < i:
        while f <= i:
            print(i, end=' ', flush=True)
            sleep(v)
            i -= p

    print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)

print('-=' * 20)
print('Agora é sua vez de persoalizar a contagem!')

i = int(input('Início: '))
f = int(input('Fim:    '))
p = int(input('Passo:  '))
v = float(input('Velocidade (s):  '))

contador(i, f, p, v)
