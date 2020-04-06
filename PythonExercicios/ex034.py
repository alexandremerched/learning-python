s = int(input("Digite o seu salário: "))

if s > 1250:
    print("Seu salário com aumento vai ser de {:.2f} R$".format(s + ( s * ( 10 / 100 ))))
else:
    print("Seu salário com aumento vai ser de {:.2f} R$".format(s + ( s * ( 15 / 100 ))))
