values = [[], []]

for c in range(0, 7):
    dados = (int(input(f'Digite o {c+1}° valor: ')))
    if dados % 2 == 0:
        values[0].append(dados)
    else:
        values[1].append(dados)
    
values[0].sort()
values[1].sort()

print('-=' * 30)
print(f'Os valores pares digitados foram: {values[0]}\nOs valores ímpares digitados foram: {values[1]}')