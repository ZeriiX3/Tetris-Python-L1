import random
import os
from math import *
from blocs import *
from form import *
import sys

# APPLICATION
run = True

def start():        # Fonction pour demander les instructions de l'utilisateur au début du jeu
    start = 0
    while start != 1 and start != 2 and start != 999:
        '''os.system("clear") # Mac '''
        os.system('cls')  # Windows
        bienvenue()
        print("Tapez 1 pour commencer à jouer")
        print("Tapez 2 pour afficher les règles")
        print("Tapez 999 pour arrêter la partie")
        print(">>>", end=" ")
        try:
            start = int(input())
        except ValueError:
            pass
    if start == 1:
        taille = 0
        try:
            taille = int(
                input("Entrez une dimension du plateau entre 21 et 26 inclus: "))  # Définition de la taille du plateau
        except ValueError:
            pass
        while taille < 21 or taille>26:
            '''os.system("clear") # Mac '''
            os.system('cls')  # Windows
            print("Valeur incorrecte ou trop grande/petite!")
            try:
                taille = int(input("Entrez une dimension du plateau entre 21 et 26 inclus: "))
            except ValueError:
                pass

    if start == 2:  # Règle du jeu
        regle_jeu()  # Affiche les règles du jeu
        print()

        s = 0
        while s != 1:
            '''os.system("clear") # Mac '''
            os.system('cls')  # Windows
            try:
                s = int(input("Tapez 1 pour commencer à jouer\n>>> "))
            except ValueError:
                pass
        if s == 1:
            taille = 0
            '''os.system("clear") # Mac '''
            os.system('cls')  # Windows
            try:
                taille = int(input(
                    "Entrez une dimension du plateau entre 21 et 26 inclus: "))  # Définition de la taille du plateau
            except ValueError:
                pass
            if taille == 999:
                print("Vous avez arrêté la partie")
                sys.exit()
            while taille > 26 or taille < 21:
                '''os.system("clear") # Mac '''
                os.system('cls')  # Windows
                print("Valeur incorrecte ou trop grande/petite!")
                try:
                    taille = int(input("Entrez une dimension du plateau entre 21 et 26 inclus: "))
                except ValueError:
                    pass


    if start == 999:
        print("Vous avez arrêté la partie")
        sys.exit()

    return taille

# ------------------------------------------------------------------------------

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
        for k in range(i + 1):
            grid_triangle[i][mid - k] = 1
            grid_triangle[i][mid + k] = 1
    del grid_triangle[mid + 1:]
    return grid_triangle


# Création du plateau LOSANGE

def grid_creation_losange(n):
    grid_losange = grid_creation_triangle(n)[:len(grid_creation_triangle(n)) - 1]
    grid_losange += grid_creation_triangle(n)[::-1]
    return grid_losange


# Création du plateau CERCLE

def grid_creation_cercle(taille):
    grid_cercle = []
    r = taille / 2 - .5
    for i in range(taille):
        ligne = []
        for j in range(taille):
            if sqrt((i - r) ** 2 + (j - r) ** 2) <= r + 0.25:
                ligne.append(1)
            else:
                ligne.append(0)
        grid_cercle.append(ligne)
    return grid_cercle


# ------------------------------------------------------------------------------


# Symboles ASCII

def symb(val):
    if val == 0:
        return " "
    elif val == 1:
        return "□"
    elif val == 2:
        return "■"


def symb_bloc(val):
    if val == 0:
        return " "
    elif val == 1:
        return "■"

# ------------------------------------------------------------------------------


# Affichage du plateau

def plateau(grid):
    for i in range(len(grid)):
        print(majuscule[i] + " " + "║", end=" ")  # affiche la lettre majuscule + la colonne
        for j in range(len(grid[i])):
            print(symb(grid[i][j]), end=" ")  # affiche les éléments de la matrice grid correspondant au plateau
        print("║")


def print_grid(mat):  # Plateau + Cadre
    '''os.system("clear") # Mac '''
    os.system('cls')  # Windows

    longueur = len(mat[0])

    # affiche les lettres minuscules en lignes
    print("    ", end="")
    for lettres in minuscule[:longueur]:
        print(lettres, end=" ")
    print("\n  ", end="")

    # affiche la première ligne du cadre
    print("╔", end="")
    print("═" * (2 * longueur + 1), end="")
    print("╗")

    plateau(mat)  # affichage du plateau à partir de la fonction
    print("  ", end="")
    print("╚" + "═" * (2 * longueur + 1) + "╝")  # affiche la dernière ligne du cadre


# ------------------------------------------------------------------------------


def select_mode():  # Demande à l'utilisateur de choisir un mode de jeu
    mode = 0
    while mode != 1 and mode != 2:
        '''os.system("clear") # Mac '''
        os.system('cls')  # Windows
        print()
        print("Tapez 1 pour afficher tout les blocs")
        print("Tapez 2 pour afficher 3 blocs au hasard")
        print(">>>", end=" ")
        try:
            mode = int(input())
        except ValueError:
            pass
    if mode == 1:
        x = 1
    elif mode == 2:
        x = 2
    return x

# ------------------------------------------------------------------------------

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

# ------------------------------------------------------------------------------

def row_state(grid, i):     # Vérifie si la ligne est pleine ou pas
    ligne_pleine = True
    for m in grid[i]:
        if m == 1:
            ligne_pleine = False
    return ligne_pleine

def col_state(grid, j):     # Vérifie si la colonne est pleine ou pas
    col_pleine = True
    for k in range(len(grid)):
            if grid[k][j] == 1:
                col_pleine = False
    return col_pleine


def row_clear(grid, i):     # Supprime tous les éléments d'une ligne pleine
    for j in range(len(grid[i])):
        if grid[i][j] == 2:
            grid[i][j] = 1

def col_clear(grid, j):     # Supprime tous les éléments d'une colonne pleine
    score_colonne = 0
    for n in range(len(grid)):
        if grid[n][j] == 2:
            grid[n][j] = 1
            score_colonne += 1
    return score_colonne


# ------------------------------------------------------------------------------


# Fonction qui laisse l'utilisateur choisir un bloc et les coordonnées où il sera poser

def longueur_max(indice):       # Prend un bloc et mesure sa longueur max
    x = 0
    for i in range(5):
        for j in range(5):
            if bloc_list[indice][j][i] == 1:
                x += 1
                break
    return x


def hauteur_max(indice):        # Prend un bloc et mesure sa hauteur max
    y = 0
    for i in range(5):
        for j in range(5):
            if bloc_list[indice][i][j] == 1:
                y += 1
                break
    return y

# --------------- Fonction qui permet de voir si un bloc choisi peut être placé ou pas ---------------------

def valid_position (grid, j, i, indice):
    placement = True
    cpt_ligne = -1
    cpt_col = -1
    try:
        for y in range(4,4-hauteur_max(indice), -1):
            cpt_ligne += 1
            for x in range(longueur_max(indice)):
                cpt_col += 1
                if bloc_list[indice][y][x] == 1:
                    if grid[i - cpt_ligne][j + cpt_col] != 1 :
                        placement = False
            cpt_col = -1
    except IndexError:
        if bloc_list[indice][y][x] == 1:
            placement = False
    return placement



def place_bloc(grid,j,i,indice):        #  Permet de placer le bloc choisi à la position donné pas l'utilisateur
    if valid_position(grid, j, i, indice) is True:
        cpt_ligne = -1
        cpt_col = -1
        for y in range(4,4-hauteur_max(indice), -1):
            cpt_ligne += 1
            for x in range(longueur_max(indice)):
                cpt_col += 1
                if bloc_list[indice][y][x] == 1 and grid[i - cpt_ligne][j + cpt_col] == 1:
                    grid[i - cpt_ligne][j + cpt_col] = 2
            cpt_col = -1
    else :
        print("La position n'est pas valide ! ")
        print("Vous avez perdu une vie")
        return False


def select_bloc(choix_plateau):         # Permet à l'utilisateur de choisir le bloc qu'il veut placer
    print("----------------------------------------------------------")
    print()
    if choix_plateau == 1:
        l = triangle_list
    elif choix_plateau == 2:
        l = losange_list
    elif choix_plateau == 3:
        l = cercle_list
    index = -1
    print("Veuillez sélectionner le bloc à positioner")
    while index not in l:
        try:
            index = int(input(">>> "))
        except ValueError:
            pass

    print("Entrez la position où vous voulez poser le bloc choisi ci-dessous:")
    for i in bloc_list[index]:
        for element in i:
            print(symb_bloc(element), end=" ")
        print()
    print(index)
    return index


# -------------- Convertit les coordonnées alphabetique en chiffre ----------------------

def coord_x():
    print()
    print("Coordonnée en x (lettre en minuscule) : ")
    x = str(0)
    while x not in minuscule:
        try:
            x = input(">>> ")
        except ValueError:
            pass
    for cle in alph_index.keys():
        if x == cle:
            return alph_index[cle]


def coord_y():
    print()
    print("Coordonnée en y (lettre en majuscule) : ")
    y = str(0)
    while y not in majuscule:
        try:
            y = input(">>> ")
        except ValueError:
            pass
    for cle in alph_index_majuscule.keys():
        if y == cle:
            return alph_index_majuscule[cle]
