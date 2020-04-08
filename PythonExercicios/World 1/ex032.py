year = int(input("Digite um ano: "))

if year % 4 == 0:
    print("{} é um ano bissexto!".format(year))
else:
    print("{} não é um ano bissexto".format(year))
