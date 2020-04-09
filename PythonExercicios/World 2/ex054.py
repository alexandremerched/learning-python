from datetime import datetime

s = 0

for i in range(0, 7):
    idade = int(input("Digite seu ano de nascimento: "))
    if int(datetime.now().year) - idade >= 21:
        s += 1

print("De 7 pessoas, {} alcançaram a maior idade e {} ainda não.".format(s, 7 - s))
