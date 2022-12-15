import os



# Mise en forme

def bienvenue():
    '''os.system("clear") # Mac '''
    os.system('cls')    # Windows

    print()
    print(45*" ", end="")
    print("╔", end="")
    print("═" * 75, end="")
    print("╗")
    print(45*" ", end="")
    print("║" + 27 * " " + "BIENVENUE SUR TETRIS" + 28 * " " + "║")
    print(45*" ", end="")
    print("╚" + "═" * 75 + "╝")
    print()




def regle_jeu():
    '''os.system("clear") # Mac '''
    os.system('cls')  # Windows

    print()
    print(45 * " ", end="")
    print("╔", end="")
    print("═" * 75, end="")
    print("╗")
    print(45 * " ", end="")
    print("║" + 30 * " " + "RÈGLES DU JEU" + 32 * " " + "║")
    print(45 * " ", end="")
    print("╚" + "═" * 75 + "╝")
    print()

    print(55 * " ", end="")
    print("blabla")
    print(55 * " ", end="")
    print("blablabla")