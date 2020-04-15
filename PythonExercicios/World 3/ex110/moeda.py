def metade(n=0, formato=False):
    res = n / 2
    return res if not formato else moeda(res)


def dobro(n=0, formato=False):
    res = n * 2
    return res if not formato else moeda(res)


def aumentar(n=0, per=0, formato=False):
    res = n + (n * (per / 100))
    return res if not formato else moeda(res)


def diminuir(n=0, per=0, formato=False):
    res = n - (n * (per / 100))
    return res if not formato else moeda(res)


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')


def resumo(preço=0, per1=0, per2=0):
    print('-'*30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-'*30)
    print(f'Preço analisado:    {moeda(preço):<}')
    print(f'Dobro do preço:     {dobro(preço, True):<}')
    print(f'Metade do preço:    {metade(preço, True):<}')
    print(f'{per1}% de aumento:     {aumentar(preço, per1, True):<}')
    print(f'{per2}% de redução:     {diminuir(preço, per2, True):<}')
    print('-'*30)
