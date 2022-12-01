import random
import os
from math import *
from blocs import *
from form import *


# APPLICATION

def start():
    start = 0
    while start != 1 and start != 2:
        print("Tapez 1 pour commencer à jouer")
        print("Tapez 2 pour afficher les règles")
        print(">>>", end=" ")
        start = int(input())
    if start == 1:
        taille = int(input("Entrez une dimension du plateau entre 21 et 35 inclus: "))  # Définition de la taille du plateau
        while taille < 21 or taille > 35:
            print("Valeur trop grande/petite!")
            taille = int(input("Entrez une nouvelle dimension : "))

    if start == 2:          # Règle du jeu
        regle_jeu()     # Affiche les règles du jeu
        print()

        s = int(input("Tapez 1 pour commencer à jouer\n>>> "))
        while s != 1:
            s = int(input("Tapez 1 pour commencer à jouer\n>>> "))
        if s == 1:
            taille = int(input("Entrez une dimension du plateau entre 21 et 35 inclus: "))  # Définition de la taille du plateau
            while taille < 21 or taille > 35:
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
    for i in range(taille):
        ligne = []
        for j in range(taille):
            if sqrt((i-r)**2 + (j-r)**2) <= r + 0.25:
                ligne.append(1)
            else:
                ligne.append(0)
        grid_cercle.append(ligne)
    return grid_cercle


# Symboles ASCII

def symb(val):
    if val == 0:
        return " "
    elif val == 1:
        return "◇"
    elif val == 2:
        return "◆"

def symb_blocs(val):
    if val == 0:
        return " "
    elif val == 1:
        return "◆"


# Affichage du plateau

def plateau(grid):
    for i in range(len(grid)):
        print(majuscule[i] + " " + "║", end=" ") # affiche la lettre majuscule + la colonne
        for j in range(len(grid[i])):
            print(symb(grid[i][j]), end=" ")   # affiche les éléments de la matrice grid correspondant au plateau
        print("║")


def print_grid(mat):             # Plateau + Cadre
    os.system("clear")  # Mac
    """os.system('cls')    # Windows"""

    longueur = len(mat[0])

    # affiche les lettres minuscules en lignes
    print("    ", end="")
    for lettres in minuscule[:longueur]:
        print(lettres, end=" ")
    print("\n  ", end="")

    # affiche la première ligne du cadre
    print("╔", end="")
    print("═"* (2 * longueur + 1), end="")
    print("╗")

    plateau(mat) # affichage du plateau à partir de la fonction
    print("  ", end="")
    print("╚" + "═"*(2 * longueur + 1) + "╝") # affiche la dernière ligne du cadre


# Affichage des BLOCS

def print_blocs(condition):      # Affiche les blocs selon le type de plateau
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


def print_random_blocs(condition):          # Affiche 3 Blocs au hasard selon le type du plateau
    print()
    list_rand = []         # Def d'une liste qui aura 3 index au hasard selon le plateau

    if condition == 1:  # Triangle
        list_rand = random.sample(triangle_list,3)      # Prend 3 index au hasard
        for i in list_rand:
            for j in bloc_list[i]:
                for k in j:
                    print(symb_blocs(k), end=" ")
                print()
            print()
    elif condition == 2:  # Losange
        list_rand = random.sample(losange_list, 3)
        for i in list_rand:
            for j in bloc_list[i]:
                for k in j:
                    print(symb_blocs(k), end=" ")
                print()
            print()
    elif condition == 3:  # Cercle
        list_rand = random.sample(cercle_list, 3)
        for i in list_rand:
            for j in bloc_list[i]:
                for k in j:
                    print(symb_blocs(k), end=" ")
                print()
            print()


def select_bloc():     # Demande à l'utilisateur de choisir un mode de jeu
    mode = 0
    while mode != 1 and mode != 2:
        print()
        print("Tapez 1 pour afficher tout les blocs")
        print("Tapez 2 pour afficher 3 blocs au hasard")
        print(">>>",end=" ")
        mode = int(input())
    if mode == 1:
        x = 1
    elif mode == 2:
        x = 2
    return x


# Stockage dans un ficher

def save_grid(grid):
    with open("plateau.txt", "w") as f_plateau:
        for i in grid:
            for j in i:
                f_plateau.write(str(j))
                f_plateau.write(" ")
            f_plateau.write("\n")
        f_plateau.close()


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