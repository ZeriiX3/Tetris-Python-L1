from fonctions import *
from blocs import *
from form import *
from screen import *

run_game = True


while run_game:

    taille = start()    # Début du jeu

    choix_plateau = 0

    while choix_plateau != 1 and choix_plateau !=2 and choix_plateau != 3:
        '''os.system("clear") # Mac '''
        os.system('cls')  # Windows
        print("Sélectionez votre plateau")
        print("1: TRIANGLE\n2: LOSANGE\n3: CERCLE")
        try:
            choix_plateau = int(input(">>> "))
        except ValueError:
            pass

    if choix_plateau == 1:
        mat = grid_creation_triangle(taille)
    elif choix_plateau == 2:
        mat = grid_creation_losange(taille)
    elif choix_plateau == 3:
        mat = grid_creation_cercle(taille)


    choix_mode = select_mode()      # Choisis le mode de jeu

    init_screen(screen, choix_mode)

    vies = 3
    while vies >= 0:
        print_grid(mat)                                    # Affiche le plateau
        affiche_tout(screen, choix_plateau, choix_mode)    # Affiche les blocs possibles à placer
        indice = select_bloc(choix_plateau)            # Selectionne le bloc choisis par l'utilisateur
        if choix_mode == 2:
            while indice >2 :
                print(">>> ")
                indice = select_bloc(choix_plateau)
        print_grid(mat)                                    # Affiche le plateau
        x,y = int(coord_x()), int(coord_y())               # Selectionne les coordonnées choisies par l'utilisateur
        if place_bloc(mat, x, y,indice) is False:          # Vérifie et place le bloc si possible, cas contraire -> perte d'une vie
            vies -= 1
            print("Nombre de vies restantes : ", vies)
        for i in range(len(mat)):
            if row_state(mat, i) is True:
                print_grid(mat)
                row_clear(mat, i)
                #mettre un clear ici bg


    save_grid(mat) # Stock le plateau dans le ficher PLATEAU.TXT

    run_game = False
