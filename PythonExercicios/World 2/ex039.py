idade = int(input("Digite o seu ano de nascimento: "))

idade = 2020 - idade

if idade < 18:
    print("Vai ter que se alistar daqui {} anos".format(18 - idade))
elif idade == 18:
    print("Hora de se alistar!!!!!!")
else:
    print("Passou {} anos do tempo de alistamento".format(idade - 18))
    