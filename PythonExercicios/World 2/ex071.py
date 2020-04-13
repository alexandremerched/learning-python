print('=' * 30)
print('{:^30}'.format('BANCO DEV'))
print('=' * 30)

c_50 = c_20 = c_10 = c_1 = 0
valor = int(input("Que valor você quer sacar? R$"))

while valor - 50 >= 0:
    valor -= 50
    c_50 += 1

if c_50 != 0:
    print(f"Total de {c_50} cédulas de R$50")

while valor - 20 >= 0:
    valor -= 20
    c_20 += 1

if c_20 != 0:
    print(f"Total de {c_20} cédulas de R$20")

while valor - 10 >= 0:
    valor -= 10
    c_10 += 1

if c_10 != 0:
    print(f"Total de {c_10} cédulas de R$10")

while valor - 1 >= 0:
    valor -= 1
    c_1 += 1

if c_1 != 0:
    print(f"Total de {c_1} cédulas de R$1")

print("==============================\nVolte sempre ao BANCO DEV! Tenha um bom dia!")
