values = []
SorN = 'S'
c = 0

while True:
    values.append(int(input('Digite um valor: ')))

    if values.count(values[c]) == 0 or values.count(values[c]) == 1:
        print('Valor adicionado com sucesso...')
        c += 1
    else:
        print('Valor duplicado! Não vou adicionar...')
        values.pop(c)

    SorN = input('Quer continuar? [S/N] ').upper()

    while SorN != 'S' and SorN != 'N':
        SorN = input('Quer continuar? [S/N] ').upper()

    if SorN == 'N':
        break

values.sort()
print('-=' * 30)
print(f'Você digitou os valores {values}')
