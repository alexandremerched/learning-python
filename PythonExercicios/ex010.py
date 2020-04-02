reais = float(input("Quanto tem na sua carteira: "))
dolar = reais/5.25

if dolar > 50:
    print("Você consegue comprar {:.2f} US$ :)".format(dolar))
else:
    print("Você consegue comprar {:.2f} US$ :(".format(dolar))
