largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))

area = largura*altura

tintaParede = area/2

print("A área da parede é {}m², que precisa de".format(area), end=' ')
print("{} litros de tinta para ser preenchida".format(tintaParede))
