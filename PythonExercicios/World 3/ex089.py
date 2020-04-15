alunos = []
nome = []
notas = []
opc = 0

while True:
    nome.append(input('Nome: '))
    notas.append(float(input('Nota 1: ')))
    notas.append(float(input('Nota 2: ')))
    nome.append(notas[:])
    alunos.append(nome[:])
    
    notas.clear()
    nome.clear()

    SorN = input('Quer continuar? [S/N] ').upper()

    while SorN != 'S' and SorN != 'N':
        SorN = input('Tente novamente.\nQuer continuar? [S/N] ').upper()

    if SorN == 'N':
        break

nome = ['a', 'bc', 'def', 'ghij']

print('-=' * 30)
print(f'No. NOME{"MÉDIA":>16}')
print('-' * 30)

for pos, a in enumerate(alunos):
    print(f'{pos:<4}{alunos[pos][0]:<10}{(alunos[pos][1][0] + alunos[pos][1][1]) / 2:>9.1f}')

while True:
    print('-' * 30)
    opc = int(input('Mostra notas de qual aluno? (999 interrompe): '))

    if opc == 999:
        break
    
    if opc < len(alunos):
        print(f'Notas de {alunos[opc][0]} são {alunos[opc][1]}')

print('FINALIZANDO...\n<<< VOLTE SEMPRE >>>')
