values = []

for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > values[-1]:
        values.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(values):
            if n <= values[pos]:
                values.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
            
print('-=' * 30)
print(f'Os valores digitados em ordem foram {values}')