from fonctions import *
from blocs import *
from form import *
from screen import *
import time

bienvenue() # Affichage de texte

time.sleep(2)

taille = start()    # Début du jeu


print("Sélectionez votre plateau")
print("1: TRIANGLE\n2: LOSANGE\n3: CERCLE")
choix_plateau = 0
try :
    choix_plateau = int(input(">>> "))
except ValueError:
    pass

while choix_plateau != 1 and choix_plateau !=2 and choix_plateau != 3:
    '''os.system("clear") # Mac '''
    os.system('cls')  # Windows
    print("Sélectionez votre plateau")
    print("1: TRIANGLE\n2: LOSANGE\n3: CERCLE")
    try:
        choix_plateau = int(input(">>> "))
    except ValueError:
        pass

if choix_plateau == 1:
    mat = grid_creation_triangle(taille)
elif choix_plateau == 2:
    mat = grid_creation_losange(taille)
elif choix_plateau == 3:
    mat = grid_creation_cercle(taille)


choix_mode = select_bloc()      # Choisis le mode de jeu

print_grid(mat)  # Affiche le plateau du jeu

affiche_tout(screen,choix_plateau,choix_mode)  # Affiche les blocs selon le type de plateau

save_grid(mat) # Stock le plateau dans le ficher PLATEAU.TXT