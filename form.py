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
    print("Vous devrez choisir une dimension XY pour le plateau désiré 
    print(55 * " ", end="")          
    print("Vous aurez le choix entre un triangle, un losange et un cercle")
    print(55 * " ", end="")
    print("Vous devrez ensuite choisir entre 2 modes de jeu :")
    print(55 * " ", end="")
    print("Le mode facile vous permet de choisir de placer n'importe quel bloc possible pour le plateau choisi")      
    print(55 * " ", end="")
    print("Le mode difficile vous restreint à 3 blocs aléatoire parmi les blocs possibles pour ce même plateau")
    print(55 * " ", end="")
    print("Ce mode vous permettera néanmoins d'obtenir plus de points pour chaque ligne ou colonne complétée")
    
