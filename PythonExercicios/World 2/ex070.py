menor = total = m_1000 = 0

while True:
    produto = input("\nDigite o nome do produto: ")
    valor = int(input("Digite o valor do produto: R$ "))
    
    total += valor
    
    if valor > 1000:
        m_1000 += 1
    
    if valor < menor or menor == 0:
        menor = valor
        produto_b = produto
           
    on_off = input("\nVocê quer continuar [S/N]: ").upper()
    
    if on_off == 'N':
        break
    
print(f"\nO total gasto na compra é de R$ {total}\nTem {m_1000} produto(s) acima de R$ 1000\nO produto mais barato é {produto_b} de R$ {menor}")
    