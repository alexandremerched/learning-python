n1 = float(input("Digite sua 1° nota: "))
n2 = float(input("Digite sua 2° nota: "))

media = (n1 + n2) / 2

if media >= 7:
    print("APROVADO")
elif media <= 6.9 and media >= 5:
    print("RECUPERAÇÃO")
else:
    print("REPROVADO")
