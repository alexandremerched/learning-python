a = int(input("Digite o comprimento de a: "))
b = int(input("Digite o comprimento de b: "))
c = int(input("Digite o comprimento de c: "))

if a + b > c and a + c > b and b + c > a:
    print("Pode se formar um triângulo") 
else:
    print("Não pode se formar um triângulo")