from fonctions import *


n = int(input("Entrez la dimension du plateau : "))
grid_creation_triangle(n)
grid_stock_triangle(grid_creation_triangle(n))

grid_creation_losange(n)
grid_stock_losange(grid_creation_losange(n))


'''
print("1: TRIANGLE\n2: LOSANGE\n3: CERCLE")
k = int(input("Sélectionez votre plateau : "))
'''
