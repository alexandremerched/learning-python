def notas(*n, sit=False):
    """
    -> Função para analizar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma. 
    """
    
    dados = {}
    maior = menor = s = 0

    for i, v in enumerate(n):
        s += v
        if i == 0:
            maior = menor = v
        elif maior < v:
            maior = v
        elif menor > v:
            menor = v

    dados['total'] = len(n)
    dados['maior'] = maior
    dados['menor'] = menor
    dados['média'] = s / len(n)

    if sit:
        if dados['média'] >= 7:
            dados['situação'] = 'BOA'
        elif 5 <= dados['média'] < 7:
            dados['situação'] = 'RAZOAVEL'
        else:
            dados['situação'] = 'RUIM'

    return dados


# Programa Principal
resp = notas(3.5, 2, 6.5, 2, 7, 4, sit=True)
print(resp)
