frase = str(input("Escreva uma frase: "))

if frase.replace(' ', '')[::-1] == frase.replace(' ', ''):
    print("É um palíndromo")
else:
    print("Não é um palíndromo")