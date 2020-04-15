grupo = []
pessoa = {}
maiores = []
pessoas = media =  0

while True:
    pessoa['nome'] = input('Nome: ')
    pessoa['sexo'] = input('Sexo: [M/F] ').upper()
    while pessoa['sexo'] != 'M' and pessoa['sexo'] != 'F':
        pessoa['sexo'] = input('Tente novamente.\nSexo: [M/F] ').upper()
    pessoa['idade'] = int(input('Idade: '))
    media += pessoa['idade']
    
    if pessoa['idade'] > 22:
        maiores.append(pessoa['nome'])
    
    grupo.append(pessoa.copy())
    pessoa.clear()
    pessoas += 1
    
    SorN = input('Quer continuar? [S/N] ').upper()

    while SorN != 'S' and SorN != 'N':
        SorN = input('Tente novamente.\nQuer continuar? [S/N] ').upper()

    if SorN == 'N':
        break
  
media = media / pessoas
    
print('-=' * 30)
print(f'- O grupo tem {pessoas} pessoas.\n- A média de idade é de {media} anos.\n- As mulheres cadastradas foram:', end=' ')

for c in grupo:
    for v in c['sexo']:
        if v == 'F':
            print(c['nome'], end=' ')
            
print('\n- Lista das pessoas que estão acima da média: ')

for c in grupo:
    if c['nome'] in maiores:
        print(f'\nnome = {c["nome"]}, sexo = {c["sexo"]}, idade = {c["idade"]}.')
            
print('<< ENCERRADO >>')
