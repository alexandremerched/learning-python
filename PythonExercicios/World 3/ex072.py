numbers = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte'

num = int(input("Digite um número entre 0 e 20: "))

while num < 0 or num > 20:
    print("Tente novamente.")
    num = int(input("Digite um número entre 0 e 20: "))
    
print(f"Você digitou o número {numbers[num]}")
