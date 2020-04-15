from random import randint
from time import sleep


def sorteia(lst):
    print('Sorteando 5 valores da lista:', end=' ')

    for i in range(0, 5):
        lst.append(randint(1, 10))
        print(lst[i], end=' ', flush=True)
        sleep(0.5)

    print('PRONTO!')


def somaPar(lst):
    s = 0

    for v in lst:
        if v % 2 == 0:
            s += v

    print(f'Somando os valores pares de {lst}, temos {s}')


lista = []

sorteia(lista)
somaPar(lista)
