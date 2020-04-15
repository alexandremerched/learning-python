pessoas = []
dados = []
SorN = 'S'
c = maior = menor = 0

while True:
    dados.append(input('Nome: '))
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])

    if c == 0:
        maior = menor = dados[1]
    elif dados[1] > maior:
        maior = dados[1]
    elif dados[1] < menor:
        menor = dados[1]

    dados.clear()
    c += 1

    SorN = input('Quer continuar? [S/N] ').upper()

    while SorN != 'S' and SorN != 'N':
        SorN = input('Tente novamente.\nQuer continuar? [S/N] ').upper()

    if SorN == 'N':
        break

print('-=' * 30)
print(f'Ao todo, você cadastrou {c} pessoas.\nO maior peso foi de {maior}Kg, Peso de', end=' ')

for i, c in enumerate(pessoas):
    if pessoas[i][1] == maior:
        print(pessoas[i][0], end=', ')

print(f'\nO menor peso foi de {menor}Kg, Peso de', end=' ')

for i, c in enumerate(pessoas):
    if pessoas[i][1] == menor:
        print(pessoas[i][0], end=', ')
