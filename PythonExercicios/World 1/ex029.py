v = int(input("Qual era a velocidade do carro: "))

if v > 80:
    multa = (v - 80) * 7
    print("Você ultrapassou a velocidade limite, sua multa é de R${}".format(multa))
else:
    print("Continue abaixo de 80Km/h")
