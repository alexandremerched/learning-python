casa = int(input("Qual é o valor da casa: R$"))
salário = int(input("Qual é o valor do salário: R$"))
anos = int(input("Em quantos anos vai pagar: "))

pagamento = casa / (anos * 12)

if pagamento < salário + salário * (30 / 100):
    print("Seu empréstimo foi aprovado!")
else:
    print("Seu empréstimo foi negado!")
