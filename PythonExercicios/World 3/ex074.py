from random import randint

atual = maior = menor = 0
numbers = randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9)

for pos, c in enumerate(numbers):
    if numbers[pos] > maior:
        maior = numbers[pos]
    if numbers[pos] < menor or menor == 0:
        menor = numbers[pos]

print(f"Os valores sorteador foram: {numbers}\nO maior número sorteado foi {maior}\nO menor número sorteado foi {menor}")