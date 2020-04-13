n = int(input("Digite um número inteiro: "))
F1 = Ft = 0
F2 = 1

print("0 -> 1 ->", end=' ')

while n != 0:
    Ft = F1 + F2
    F1 = F2
    F2 = Ft
    n -= 1

    print("{} ->".format(Ft), end=' ')
