num = int(input("Digite um número para ser fatorado: "))
result = num 

while num != 1:
    num -= 1
    result *= num
    
print(result)