num = int(input("Digite o primeiro termo: "))
r = int(input("Digite a razão: "))
c = t = 0

while True:
    while c != 10:
        print("{}".format(num), end=' ')
        num += r
        c += 1

    print("")
    t = int(input("Quantos termos vc ainda quer ver: "))

    if t == 0:
        break
    elif t > 0:
        while t != 0:
            print("{}".format(num), end=' ')
            num += r
            t -= 1
    