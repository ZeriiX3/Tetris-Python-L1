from fonctions import *
from blocs import *
from form import *


bienvenue() # Affichage de texte

taille = start()    # Début du jeu


print("Sélectionez votre plateau")
print("1: TRIANGLE\n2: LOSANGE\n3: CERCLE")
choix_plateau = int(input(">>> "))
while choix_plateau != 1 and choix_plateau !=2 and choix_plateau != 3:
    print("Sélectionez votre plateau")
    print("1: TRIANGLE\n2: LOSANGE\n3: CERCLE")
    choix_plateau = int(input(">>> "))
if choix_plateau == 1:
    mat = grid_creation_triangle(taille)
elif choix_plateau == 2:
    mat = grid_creation_losange(taille)
elif choix_plateau == 3:
    mat = grid_creation_cercle(taille)


choix_mode = select_bloc()      # Choisis le mode de jeu
print_grid(mat)  # Affiche le plateau du jeu


if choix_mode == 1:
    print_blocs(choix_plateau)              # Affiche tous les BLOCS
if choix_mode == 2:
    print_random_blocs(choix_plateau)       # Affiche 3 blocs au hasard


save_grid(mat) # Stock le plateau dans le ficher PLATEAU.TXT
