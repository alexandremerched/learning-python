d = int(input("Qual a distância de viagem: "))

if d <= 200:
    print("Você vai pagar R${}".format(d * 0.5))
elif d > 200:
    print("Você vai pagar R${}".format(d * 0.45))