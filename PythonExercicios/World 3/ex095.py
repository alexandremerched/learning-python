jogadores = []
dados = {}
gols = []
count = total = 0

while True:
    print('-'*30)
    dados['nome'] = input('Nome do Jogador: ')
    count = int(input(f'Quantas partidas {dados["nome"]} jogou? '))

    for c in range(0, count):
        gols.append(int(input(f'    Quantos gols na partida {c+1}? ')))
        total += gols[c]

    dados['gols'] = gols[:]
    dados['total'] = total

    jogadores.append(dados.copy())
    dados.clear()
    gols.clear()
    total = 0

    SorN = input('Quer continuar? [S/N] ').upper()

    while SorN != 'S' and SorN != 'N':
        SorN = input('Tente novamente.\nQuer continuar? [S/N] ').upper()

    if SorN == 'N':
        break

print('-='*30)
print(f'cod {"nome":<15}{"gols":<15}{"total":<15}')
print('-'*40)
for pos, v in enumerate(jogadores):
    print(f'{pos:>3} {v["nome"]:<15}{str(v["gols"]):<15}{v["total"]:<15}')

while True:
    print('-' * 40)
    opc = int(input('Mostra dados de qual jogador? (999 para parar) '))

    if opc == 999:
        break

    if opc < len(jogadores) and opc >= 0:
        print(f' -- LEVANTAMENTO DO JOGADOR {jogadores[opc]["nome"]}:')
        for i, v in enumerate(jogadores[opc]['gols']):
            print(f'   No jogo {i+1} fez {v} gols.')
    else:
        print(f'ERRO! Não existe jogador com código {opc}!')

print('<< VOLTE SEMPRE >>')
