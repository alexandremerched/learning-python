from random import randint
from time import sleep

jogo = []
num = 0

print('-' * 30)
print(f'{"JOGA NA MEGA SENA":^30}')
print('-' * 30)

jogos = int(input('Quantos jogos você quer que eu sorteie? '))

print('-=' * 3, end='  ')
print(f'SORTEANDO {jogos} JOGOS', end='  ')
print('-=' * 3)

for c in range(0, jogos):
    while len(jogo) < 6:
        num = randint(1, 60)
        if len(jogo) == 0:
            jogo.append(num)
        elif jogo.count(num) == 0:
            jogo.append(num)
        
    jogo.sort()    
    print(f'Jogo {c+1}: {jogo}')
    jogo.clear()
    sleep(1)

print('-=' * 5, end=' ')
print('< BOA SORTE! >', end=' ')
print('-=' * 5)
