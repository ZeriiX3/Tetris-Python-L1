from math import *

''' BLOCS '''

# Blocs communs
bloc_list = [[[1, 0],
              [1, 1]
              ],
             [[0, 1],
              [1, 1]
              ],
             [[1, 0, 0],
              [1, 1, 1]
              ],
             [[1, 1],
              [0, 1],
              [0, 1]
              ],
             [[1, 0],
              [1, 1],
              [1, 0]
              ],
             [[0, 1, 0],
              [1, 1, 1]
              ],
             [[1, 1, 0],
              [0, 1, 1]
              ],
             [[1, 0],
              [1, 1],
              [0, 1]
              ],
             [[1],
              [1],
              [1],
              [1]
              ],
             [[1, 1],
              [1, 1]
              ],
             [[1, 1],
              [0, 1]
              ],
             [[1, 1],
              [1, 0]
              ],
             [[0, 0, 1],
              [1, 1, 1]
              ],
             [[1, 0],
              [1, 0],
              [1, 1]
              ],
             [[0, 1],
              [1, 1],
              [0, 1]
              ],
             [[1, 1, 1],
              [0, 1, 0]
              ],
             [[0, 1, 1],
              [1, 1, 0]
              ],
             [[0, 1],
              [1, 1],
              [1, 0]
              ],
             [[1, 1, 1, 1]
              ],
             [[1]
              ],

             [[1, 1, 1, 1],          # Blocs Cercle
              [1, 1, 1, 1],
              [1, 1, 1, 1],
              [1, 1, 1, 1]
              ],
             [[0, 1, 1, 0],
              [1, 1, 1, 1],
              [1, 1, 1, 1],
              [0, 1, 1, 0]
              ],
             [[1, 0, 0, 1],
              [1, 0, 0, 1],
              [1, 0, 0, 1],
              [1, 1, 1, 1]
              ],
             [[1, 1, 1, 1],
              [0, 0, 0, 1],
              [0, 0, 0, 1],
              [0, 0, 0, 1]
              ],
             [[1, 1, 1, 1],
              [1, 1, 1, 0]
              ],
             [[1, 1, 1],
              [0, 0, 1],
              [0, 0, 1],
              [1, 1, 1]
              ],
             [[1, 1],
              [1, 1],
              [1, 1],
              [1, 1]
              ],
             [[1, 1, 1, 1],
              [1, 1, 1, 1]
              ],
             [[1],
              [1],
              [1],
              [1],
              [1]
              ],
             [[1, 1, 1, 1, 1],
              [1, 0, 0, 0, 1]
              ],
             [[1, 1, 1, 1, 1]
              ],
             [[1, 0, 0, 0],
              [1, 0, 0, 0],
              [1, 0, 0, 1],
              [1, 1, 1, 1]
              ],

             [[0, 0, 1, 1],             # Blocs losange
              [0, 1, 1, 0],
              [1, 1, 0, 0],
              [1, 0, 0, 0]
              ],
             [[1, 1, 0, 0],
              [0, 1, 1, 0],
              [0, 0, 1, 1],
              [0, 0, 0, 1]
              ],
             [[1, 1, 1, 1],
              [0, 1, 1, 0],
              [0, 1, 1, 0],
              [0, 1, 1, 0]
              ],
             [[1, 0, 0, 1],
              [0, 1, 1, 0],
              [0, 1, 1, 0],
              [1, 0, 0, 1]
              ],
             [[1, 1, 1, 1, 1],
              [0, 1, 1, 1, 0],
              [0, 0, 1, 0, 0]
              ],
             [[1, 1, 1, 1],
              [1, 1, 1, 1],
              [1, 1, 1, 1],
              [1, 1, 1, 1]
              ],
             [[1, 0, 0, 0],
              [1, 1, 0, 0],
              [0, 1, 1, 0],
              [0, 0, 1, 1]
              ],
             [[0, 0, 0, 1],
              [0, 0, 1, 1],
              [0, 1, 1, 0],
              [1, 1, 0, 0]
              ],
             [[1],
              [1],
              [1],
              [1],
              [1]
              ],
             [[0, 0, 0, 1],
              [1, 1, 1, 1],
              [0, 0, 0, 1]
              ],
             [[1, 1, 1, 1, 1],
              ],
             [[1, 1, 1, 1],
              [0, 0, 0, 1]
              ],
             [[1, 1],
              [0, 1],
              [0, 1],
              [0, 1]
              ],
             [[1, 0],
              [1, 0],
              [1, 0],
              [1, 1]
              ],

             [[1, 0, 0],                    # Blocs Triangle
              [1, 1, 1],
              [0, 0, 1],
              ],
             [[1, 1, 0],
              [0, 1, 0],
              [0, 1, 1],
              ],
             [[0, 0, 1],
              [1, 1, 1],
              [1, 0, 0],
              ],
             [[0, 1, 1],
              [0, 1, 0],
              [1, 1, 0],
              ],
             [[0, 0, 1],
              [0, 1, 0],
              [1, 0, 0]
              ],
             [[1, 0, 0],
              [0, 1, 0],
              [0, 0, 1]
              ],
             [[1],
              [1],
              [1]
              ],
             [[1, 1, 1]
              ],
             [[1],
              [1]
              ],
             [[0, 1, 0],
              [1, 1, 1],
              [0, 1, 0]
              ],
             [[1, 1]
              ]

             ]


# Index des BLOCS
cercle_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
               29, 30, 31]
losange_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 32, 33, 34, 35, 36, 37, 38,
                39, 40, 41, 42, 43, 44, 45]
triangle_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 46, 47, 48, 49, 50, 51, 52,
                 53, 54, 55, 56]


# APPLICATION





'''CREATION DES PLATEAUX'''


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
    grid_losange = []
    if n % 2 == 0:
        n -= 1
    for i in range(n):
        k = []
        for j in range(n):
            k.append(0)
        grid_losange.append(k)
    mid = len(grid_losange) // 2
    for i in range(n // 2 + 1):
        grid_losange[i][mid] = 1
        for k in range(i + 1):
            grid_losange[i][mid - k] = 1
            grid_losange[i][mid + k] = 1
    del grid_losange[mid + 1:]
    temp = []
    temp += grid_losange
    grid_losange.reverse()
    del grid_losange[0]
    temp += grid_losange
    return temp


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



# Affichage du plateau

def print_grid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print(grid[i][j], end="")
        print()

# Affichage des BLOCS


def print_blocs(grid):      # Affichage des blocs selon le type de plateau
    if grid == 1: # Triangle
        for i in triangle_list:
            print(bloc_list[i])
    elif grid == 2: # Losange
        for i in losange_list:
            print(bloc_list[i])
    elif grid == 3: # Cercle
        for i in cercle_list:
            print(bloc_list[i])

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