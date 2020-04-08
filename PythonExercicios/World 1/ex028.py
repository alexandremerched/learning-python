from random import randint

random_num = int(randint(0, 5))

num = int(input("""Vou 'pensar' em um número de 0 a 5, tente advinhar.

Digite o número que eu pensei: """))

if num == random_num:
    print("Você acertou, é o número {}!".format(random_num))
else:
    print("Você errou, o número correto era {}".format(random_num))