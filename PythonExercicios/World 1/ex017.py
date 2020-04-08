from math import hypot

c1 = int(input("Digite o cateto oposto: "))
c2 = int(input("Digite o cateto adjacente: "))

print("A hipotenusa dos catetos {} e {} é igual a {}".format(c1, c2, hypot(c1, c2)))