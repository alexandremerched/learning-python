peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / altura ** altura

if imc < 18.5:
    print("Abaixo do Peso")
elif imc < 25 and imc >= 18.5:
    print("Peso Ideal")
elif imc < 30 and imc >= 25:
    print("Sobrepeso")
elif imc < 40 and imc >= 30:
    print("Obesidade")
else:
    print("Obesidade mórbida")