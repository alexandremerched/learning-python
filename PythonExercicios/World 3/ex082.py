values = []
values_par = []
values_impar = []
SorN = 'S'

while True:
    values.append(int(input('Digite um número: ')))

    SorN = input('Quer continuar? [S/N] ').upper()

    while SorN != 'S' and SorN != 'N':
        SorN = input('Tente Novamente.\nQuer continuar? [S/N]').upper()

    if SorN == 'N':
        break

for v in values:
    if v % 2 == 0:
        values_par.append(v)
    else:
        values_impar.append(v)

print('-=' * 30)
print(f'A lista completa é {values}')
print(f'A lista de pares é {values_par}')
print(f'A lista de ímpares é {values_impar}')
