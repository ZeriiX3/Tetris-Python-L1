from math import *
from blocs import *


# APPLICATION



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


# Stock dans un ficher

def save_grid(grid):
    with open("plateau.txt", "w") as f_plateau:
        for i in grid:
            for j in i:
                f_plateau.write(str(j))
                f_plateau.write(" ")
            f_plateau.write("\n")
        f_plateau.close()

# Symboles

def sym(val):
    if val == 0:
        return " "
    elif val == 1:
        return "□"
    elif val == 2:
        return "■"


# Affichage du plateau

def print_grid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print(sym(grid[i][j]), end=" ")
        print()

# Affichage des BLOCS

'''
def print_blocs(grid):      # Affichage des blocs selon le type de plateau
    if grid == 1: # Triangle
        for i in triangle_list:
            for j in range(len(i)):
                for k in range(len(bloc_list))
            print(bloc_list[i])
    elif grid == 2: # Losange
        for i in losange_list:
            print(bloc_list[i])
    elif grid == 3: # Cercle
        for i in cercle_list:
            print(bloc_list[i])
'''


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