s = num_s = 0

while True:
    n = int(input("Digite um número: "))
    if n == 999:
        break
    num_s += 1
    s += n

print(f"Ao todo foram {num_s} números somadas, que somados são igual a {s}")
    