from fonctions import *

print("Bienvenue sur TETRIS")
start = 0
while start != 1 and start != 2:
    print("Tapez 1 pour commencer à jouer")
    print("Tapez 2 pour afficher les règles")
    start = int(input())
if start == 1:
    taille = int(input("Entrez la dimension du plateau : "))  # Définition de la taille du plateau
    while taille < 20 or taille > 41 or taille % 2 == 0:
        print("Valeur impaire ou trop grande/petite!")
        taille = int(input("Entrez une nouvelle dimension : "))
if start == 2:
    print("Voici les règles du jeu :")
    quit = int(input("1 : Commencez à jouer"))
    if quit == 1:
        taille = int(input("Entrez la dimension du plateau : "))  # Définition de la taille du plateau
        while taille < 20 or taille > 41 or taille % 2 == 0:
            print("Valeur impaire ou trop grande/petite!")
            taille = int(input("Entrez une nouvelle dimension : "))



print("1: TRIANGLE\n2: LOSANGE\n3: CERCLE")
choix_plateau = int(input("Sélectionez votre plateau : "))
if choix_plateau == 1:
    grid_creation_triangle(taille)
elif choix_plateau == 2:
    grid_creation_losange(taille)
elif choix_plateau == 3:
    grid_creation_cercle(taille)


grid_stock_triangle(grid_creation_triangle(taille))
grid_stock_losange(grid_creation_losange(taille))





print_blocs(k) # Affichage des blocs selon le type de plateau
