from random import randint

print("""
----- Jokenpô -----
        ^_^
-------------------
""")

while True:
    on_off = 1

    # PC turn #

    choice_pc = randint(1, 3)
    random = randint(1, 3)

    if random == 1:
        print("-Computador: Talvez eu jogue pedra")
    elif random == 2:
        print("-Computador: Talvez eu jogue papel")
    else:
        print("-Computador: Talvez eu jogue tesoura")

    # USER turn #

    print("""-Computador: Sua vez!
    """)

    choice_user = int(input("""Escolha entre:

1 - Pedra
2 - Papel
3 - Tesoura
4 - Sair do jogo
    
"""))

    # GAME #

    if choice_pc == 1:
        print("""
O computador jogou pedra""")
    elif choice_pc == 2:
        print("""
O computador jogou papel""")
    else:
        print("""
O computador jogou tesoura""")

    # GAME & RESULTS #

    if choice_user == 4:
        break

    elif choice_user == choice_pc:
        print("""
EMPATE!!!
              
Vamos de novo?
        
1 - Sim
2 - Não
""")
        on_off = int(input(""))
        print("")

    elif (choice_user == 1 and choice_pc == 3) or (choice_user == 2 and choice_pc == 1) or (choice_user == 3 and choice_pc == 2):
        print("""
VITÓRIA!!!
        
Vamos de novo?

1 - Sim
2 - Não
""")
        on_off = int(input(""))
        print("")

    else:
        print("""
DERROTA!!!

Vamos de novo?

1 - Sim
2 - Não
""")
        on_off = int(input(""))
        print("")

    # END GAME #

    if on_off == 2:
        break
