from datetime import datetime

dados = {}
dados['nome'] = input('Nome: ')
dados['idade'] = datetime.now().year - int(input('Ano de nascimento: '))
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Sálario: R$ '))
    dados['aposentadoria'] = 35 - (datetime.now().year - dados['contratação']) + dados['idade']
print('-=' * 30)
for k, v in dados.items():
    print(f'{k} tem o valor {v}')