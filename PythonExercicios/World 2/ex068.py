from random import randint

victories = 0

print("Vamos jogar par ou ímpar, até eu ganhar de você.")

while True:
    choice = int(input(
        "\nEscolha:\npar[1]\nímpar[2]\nsair do jogo[3]\n"))

    if choice == 1:
        num = int(input("\nSua escolha foi par, agora digite um número: "))
        num_cpu = int(randint(0, 10))

        if (num + num_cpu) % 2 == 0:
            print(f"\nO computador jogou {num_cpu}\nVocê venceu, vamos de novo")
            victories += 1
        else:
            break

    elif choice == 2:
        num = int(input("\nSua escolha foi ímpar, agora digite um número: "))
        num_cpu = randint(0, 10)

        if (num + num_cpu) % 2 == 0:
            break
        else:
            print(f"\nO computador jogou {num_cpu}\nVocê venceu, vamos de novo")
            victories += 1
            
    elif choice == 3:
        break
    
if victories == 1:    
    print(f"O computador jogou {num_cpu}\n\nVocê perdeu e ganhou {victories} vez!")
else:
    print(f"O computador jogou {num_cpu}\n\nVocê perdeu e ganhou {victories} vezes!")
