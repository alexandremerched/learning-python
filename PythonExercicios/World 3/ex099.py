from time import sleep


def maior(*num):
    maior = c = 0

    print('-=' * 30)
    print('Analizando os valores passados...')

    for v in num:
        print(v, end=' ', flush=True)
        sleep(0.5)
        if c == 0:
            maior = v
        elif v > maior:
            maior = v
        c += 1

    print(f'Foram informados {c} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
