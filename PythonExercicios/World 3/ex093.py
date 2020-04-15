dados = {}
gols = []
count = total = 0

dados['nome'] = input('Nome do Jogador: ')
count = int(input(f'Quantas partidas {dados["nome"]} jogou? '))

for c in range(0, count):
    gols.append(int(input(f'Quantos gols na partida {c+1}? ')))
    total += gols[c]

dados['gols'] = gols
dados['total'] = total

print('-=' * 30)
print(dados)
print('-=' * 30)

for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 30)

print(f'O jogador {dados["nome"]} jogou {count} partidas.')

for i, v in enumerate(gols):
    print(f'    => Na partida {i+1}, fez {v} gols.')

print(f'Foi um total de {total} gols.')
