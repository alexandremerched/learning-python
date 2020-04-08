a = int(input("Digite o comprimento de a: "))
b = int(input("Digite o comprimento de b: "))
c = int(input("Digite o comprimento de c: "))

if a + b > c and a + c > b and b + c > a:
    if a == b and a == c and b == c:
        print("É um triângulo equilátero")
    elif a == b or a == c or b == c:
        print("É um triângulo isóscele")
    else:
        print("É um triângulo escanelo")
else:
    print("Não pode se formar um triângulo")