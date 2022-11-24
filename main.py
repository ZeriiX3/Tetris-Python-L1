from fonctions import *


n = int(input("Entrez la dimension du plateau : "))
grid_creation_triangle(n)
grid_stock(grid_creation_triangle(n))


print("1: TRIANGLE\n2: LOSANGE\n3: CERCLE")
k = int(input("Sélectionez votre plateau : "))

print(read_grid(k))
