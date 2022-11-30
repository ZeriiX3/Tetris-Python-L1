from fonctions import *
from blocs import *
from form import *


bienvenue() # Affichage de texte


taille = start()    # Début du jeu


print("1: TRIANGLE\n2: LOSANGE\n3: CERCLE")
choix_plateau = int(input("Sélectionez votre plateau : "))
while choix_plateau != 1 and choix_plateau !=2 and choix_plateau != 3:
    print("1: TRIANGLE\n2: LOSANGE\n3: CERCLE")
    choix_plateau = int(input("Sélectionez votre plateau : "))
if choix_plateau == 1:
    mat = grid_creation_triangle(taille)
elif choix_plateau == 2:
    mat = grid_creation_losange(taille)
elif choix_plateau == 3:
    mat = grid_creation_cercle(taille)


print_blocs(choix_plateau)     # Affiche les BLOCS

print_grid(mat)  # Affiche le plateau du jeu

save_grid(mat) # Enregistre le plateau dans le ficher PLATEAU.TXT






