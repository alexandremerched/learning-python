from random import randint

random_num = int(randint(0, 5))
c = 1

print("Vou 'pensar' em um número de 0 a 5, tente advinhar.")
print("")
num = int(input("Digite o que eu pensei: "))

while True:
    if num == random_num:
        print("Você acertou, você levou {} tentativa(s) para acertar".format(c))
        break
    else:
        num = int(input("Você errou, tente novamente: "))
        c += 1
