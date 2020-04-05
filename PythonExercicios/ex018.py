from math import cos, sin, tan, radians

a = float(input("Digite o ângulo: "))

print("O ângulo {}° tem \nSeno:{:.2f} \nCosseno:{:.2f} \nTangente:{:.2f}".format(
    a, 
    sin(radians(a)), 
    cos(radians(a)), 
    tan(radians(a))))
