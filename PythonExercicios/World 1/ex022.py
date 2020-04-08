name = str(input("Digite seu nome completo: "))

print("{}\n{}\n{}\n{}".format(name.upper(), name.lower(), len(''.join(name.split())), len(name.split()[0])))
