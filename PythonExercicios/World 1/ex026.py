frase = input("Digite uma frase: ")

print("A frase tem {} A, o primeiro A começa na posição {} e o último A esta na posição {}"
      .format(
        frase.upper().count('A'),
        frase.upper().find('A'),
        frase.upper().rfind('A')
        )
    )
