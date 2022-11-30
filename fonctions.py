from math import *
from blocs import *


# APPLICATION

def start():
    start = 0
    while start != 1 and start != 2:
        print("Tapez 1 pour commencer à jouer")
        print("Tapez 2 pour afficher les règles")
        print(">>>", end=" ")
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
    return taille

# Création du plateau TRIANGLE

def grid_creation_triangle(n):
    grid_triangle = []
    if n % 2 == 0:
        n -= 1
    for i in range(n):
        k = []
        for j in range(n):
            k.append(0)
        grid_triangle.append(k)
    mid = len(grid_triangle) // 2
    for i in range(n // 2 + 1):
        grid_triangle[i][mid] = 1
        for k in range(i + 1):
            grid_triangle[i][mid - k] = 1
            grid_triangle[i][mid + k] = 1
    del grid_triangle[mid + 1:]
    return grid_triangle


# Création du plateau LOSANGE

def grid_creation_losange(n):
    grid_losange = grid_creation_triangle(n)[:len(grid_creation_triangle(n))-1]
    grid_losange += grid_creation_triangle(n)[::-1]
    return grid_losange


# Création du plateau CERCLE


def grid_creation_cercle(taille):
    grid_cercle =[]
    r = taille/2-.5
    for x in range(taille):
        ligne = []
        for y in range(taille):
            if sqrt((x-r)**2 + (y-r)**2) <= r + 0.25:
                ligne.append(1)
            else:
                ligne.append(0)
        grid_cercle.append(ligne)
    return grid_cercle


# Stockage dans un ficher

def save_grid(grid):
    with open("plateau.txt", "w") as f_plateau:
        for i in grid:
            for j in i:
                f_plateau.write(str(j))
                f_plateau.write(" ")
            f_plateau.write("\n")
        f_plateau.close()

# Symboles ASCII

def symb(val):
    if val == 0:
        return " "
    elif val == 1:
        return "□"
    elif val == 2:
        return "■"

def symb_blocs(val):
    if val == 0:
        return " "
    elif val == 1:
        return "■"


# Affichage du plateau

def print_grid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print(symb(grid[i][j]), end=" ")
        print()


def print_grid_cadre(mat):
    hauteur = len(mat)
    longueur = len(mat[0])

    print("    ", end="")
    for lettres in minuscule[:hauteur]:
        print(lettres, end=" ")

    print("\n  ", end="")

    print("╔", end="")
    print("═"* (2 * longueur + 1), end="")
    print("╗")

    for i in range(hauteur):
        print(majuscule[i] + " " + "║", end=" ")
        print("║")

    print("  ", end="")
    print("╚" + "═"*(2 * longueur + 1) + "╝")

# Affichage des BLOCS

def print_blocs(condition):      # Affiche les blocs selon le type de plateau
    print()
    print(30 * "=")
    print()
    if condition == 1: # Triangle
        for i in triangle_list:
            for j in bloc_list[i]:
                for k in j:
                    print(symb_blocs(k),end=" ")
                print()
            print()
    elif condition == 2: # Losange
        for i in losange_list:
            for j in bloc_list[i]:
                for k in j:
                    print(symb_blocs(k), end=" ")
                print()
            print()
    elif condition == 3: # Cercle
        for i in cercle_list:
            for j in bloc_list[i]:
                for k in j:
                    print(symb_blocs(k), end=" ")
                print()
            print()



'''
def gamemode_random():
'''


"""
def read_grid(path):
    grid = []
    if path == 1:
        with open("triangle.txt", "r") as f_t:
            cont = f_t.readlines()
            for l in cont:
                grid.append(l)
    return grid

    elif path == 2:
        return grid_losange
    elif path == 3:
        return grid_cercle
"""