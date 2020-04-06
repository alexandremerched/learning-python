n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
n3 = int(input("Digite outro número: "))

if n1 >= n2:
    if n1 >= n3:
        if n2 >= n3:
            print("O maior número é {} e o menor é {}".format(n1, n3))
        else:
            print("O maior número é {} e o menor é {}".format(n1, n2))
    else:
        print("O maior número é {} e o menor é {}".format(n3, n2))
elif n3 >= n2:
    print("O maior número é {} e o menor é {}".format(n3, n1))
elif n1 >= n3: 
    print("O maior número é {} e o menor é {}".format(n2, n3))
else:
    print("O maior número é {} e o menor é {}".format(n2, n1))