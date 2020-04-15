values = []
SorN = 'S'
c = 0

while True:
    values.append(int(input('Digite um valor: ')))
    c += 1

    SorN = input('Quer continuar? [S/N] ').upper()

    while SorN != 'S' and SorN != 'N':
        SorN = input('Quer continuar? [S/N] ').upper()
        
    if SorN == 'N':
        break

values.sort(reverse=True)
print('-=' * 30)
print(f'Você digitou {c} elementos.\nOs valores em ordem decrescente são {values}')
if 5 in values:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
