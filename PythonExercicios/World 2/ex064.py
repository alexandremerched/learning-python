result = 0
n = input("Digite um número: ")

while n != 999:
    n = int(input("Digite outro número, se quiser para digite 999: "))
    
    if n != 999:
        result += n
    elif n == 999:
        print("A soma de todos os números é {}".format(result))
        break