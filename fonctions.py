''' BLOCS '''

# Blocs communs
Bloc_list = [[[1, 0],
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
    temp = temp + grid_losange
    grid_losange.reverse()
    del grid_losange[0]
    temp += grid_losange
    return temp


'''STOCKAGE DANS FICHIER '''


# Stock dans ficher TRIANGLE.TXT

def grid_stock_triangle(grid_triangle):
    f_triangle = open("triangle.txt", "w")
    for i in grid_triangle:
        for j in i:
            f_triangle.write(str(j))
            f_triangle.write(" ")
        f_triangle.write("\n")
    f_triangle.close()


# Stock dans ficher LOSANGE.TXT

def grid_stock_losange(grid_losange):
    f_losange = open("losange.txt", "w")
    for i in grid_losange:
        for j in i:
            f_losange.write(str(j))
            f_losange.write(" ")
        f_losange.write("\n")
    f_losange.close()


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
