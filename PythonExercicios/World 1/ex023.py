num = input("Digite um número entre 0 a 9999: ")
num = num[::-1]
print('')

while len(num) == 0 or len(num) > 4:
    print("Error: Número inválido")
    print('')
    num = input("Digite um número entre 0 a 9999: ")
    print('')  

if len(num) == 1:
    print("unidade:{}".format(num))

if len(num) == 2:
    print("unidade:{}\ndezena:{}".format(
        num[0],
        num[1]
    ))

if len(num) == 3:
    print("unidade:{}\ndezena:{}\ncentena:{}".format(
        num[0],
        num[1],
        num[2]
    ))

if len(num) == 4:
    print("unidade:{}\ndezena:{}\ncentena:{}\nmilhar:{}".format(
        num[0],
        num[1],
        num[2],
        num[3]
    ))