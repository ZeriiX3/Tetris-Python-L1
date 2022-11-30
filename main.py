from fonctions import *
from blocs import *

print("Bienvenue sur TETRIS")
taille = start()


print("1: TRIANGLE\n2: LOSANGE\n3: CERCLE")             # Choix du plateau
choix_plateau = int(input("Sélectionez votre plateau : "))

if choix_plateau == 1:
    mat = grid_creation_triangle(taille)
elif choix_plateau == 2:
    mat = grid_creation_losange(taille)
elif choix_plateau == 3:
    mat = grid_creation_cercle(taille)


print_blocs(choix_plateau)     # Affiche les BLOCS

print_grid_cadre(mat)

save_grid(mat) # Enregistre le plateau dans le ficher PLATEAU.TXT






