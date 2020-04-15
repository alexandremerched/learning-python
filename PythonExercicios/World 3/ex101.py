def voto(ano):
    from datetime import datetime
    
    idade = datetime.now().year - ano

    if idade < 16:
        return f'Com {idade} anos: VOTO NEGADO.'
    elif 16 <= idade < 18 or idade >= 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    elif idade >= 18:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'


print('-'*30)
n = int(input('Em que ano você nasceu? '))
print(voto(n))
