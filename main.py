from fonctions import *
from blocs import *

print("Bienvenue sur TETRIS")
start = 0
while start != 1 and start != 2:
    print("Tapez 1 pour commencer à jouer")
    print("Tapez 2 pour afficher les règles")
    start = int(input())
if start == 1:
    taille = int(input("Entrez la dimension du plateau : "))  # Définition de la taille du plateau
    while taille < 20 or taille > 40:
        print("Valeur trop grande/petite!")
        taille = int(input("Entrez une nouvelle dimension : "))
if start == 2:
    print("Voici les règles du jeu :")
    s = int(input("1 : Commencez à jouer"))
    if s == 1:
        taille = int(input("Entrez la dimension du plateau : "))  # Définition de la taille du plateau
        while taille < 20 or taille > 40:
            print("Valeur trop grande/petite!")
            taille = int(input("Entrez une nouvelle dimension : "))



print("1: TRIANGLE\n2: LOSANGE\n3: CERCLE")             # Choix du plateau
choix_plateau = int(input("Sélectionez votre plateau : "))

if choix_plateau == 1:
    mat = grid_creation_triangle(taille)
elif choix_plateau == 2:
    mat = grid_creation_losange(taille)
elif choix_plateau == 3:
    mat = grid_creation_cercle(taille)

"""
print_blocs(choix_plateau) # Affiche les BLOCS
"""
save_grid(mat) # Enregistre le plateau dans le ficher PLATEAU.TXT
print_grid(mat)





"""
print_blocs(k) # Affichage des blocs selon le type de plateau
"""