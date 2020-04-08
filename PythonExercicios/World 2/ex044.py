price = float(input("Digite o valor do produto: R$ "))
payment = int(input("""Escolha um dos metódos de pagamento abaixo:
1 - dinheiro/cheque;
2 - cartão;
3 - 2x no cartão;
4 - 3x ou mais no cartão.

"""))

if payment == 1:
    print("Você vai pagar no total R$ {}".format(price - (price * (10 / 100))))
elif payment == 2:
    print("Você vai pagar no total R$ {}".format(price - price * (5 / 100)))
elif payment == 3:
    print("Você vai pagar no total R$ {}".format(price))
elif payment == 4:
    print("Você vai pagar no total R$ {}".format(price + price * (20 / 100)))    
