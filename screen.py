from fonctions import *

lin = 30
col = 70
screen = []

def init_screen(scr):
    for line in range(lin) :
        lst = []
        for e in range (col):
            lst.append(0)
        scr.append(lst)

def insert_bloc_screen(scr, bloc, l , c, num):
    for i in range (len(bloc)):
        for j in range(len(bloc[i])):
            pos_x = l + i
            pos_y = c + j
            screen[pos_x][pos_y] = bloc[i][j]
    screen[l + 6][c] = num


def print_screen(scr):
    for i in range (len(scr)):
        for j in range(len(scr[i])):
            if scr[i][j] == 1 :
                print("◆ ", end="")
            elif scr[i][j] == 0 :
                print("  ", end="")
            else:
                print(" {} ".format(scr[i][j]), end=" ")
        print()

init_screen(screen)

def affiche_tout(screen, choix_plateau, choix_mode):
    c = 0
    l = 0
    if choix_plateau == 1:
        if choix_mode == 1:
            for i in triangle_list:
                insert_bloc_screen(screen, bloc_list[i], l, c, str(i))
                c += 6
                if c == 66:
                    l += 7
                    c = 0
        elif choix_mode == 2:
            rand_list = random.sample(triangle_list, 3)
            for i in range(len(rand_list)):
                insert_bloc_screen(screen, bloc_list[triangle_list[i]], l, c, str(i))
                c += 6
                if c == 66:
                    l += 7
                    c = 0
    if choix_plateau == 2:
        if choix_mode == 1:
            for i in losange_list:
                insert_bloc_screen(screen, bloc_list[i], l, c, str(i))
                c += 6
                if c == 66:
                    l += 7
                    c = 0
        elif choix_mode == 2:
            rand_list = random.sample(losange_list, 3)
            for i in range(len(rand_list)):
                insert_bloc_screen(screen, bloc_list[losange_list[i]], l, c, str(i))
                c += 6
                if c == 66:
                    l += 7
                    c = 0
    if choix_plateau == 3:
        if choix_mode == 1:
            for i in cercle_list:
                insert_bloc_screen(screen, bloc_list[i], l, c, str(i))
                c += 6
                if c == 66:
                    l += 7
                    c = 0
        elif choix_mode == 2:
            rand_list = random.sample(cercle_list, 3)
            for i in range(len(rand_list)):
                insert_bloc_screen(screen, bloc_list[cercle_list[i]], l, c, str(i))
                c += 6
                if c == 66:
                    l += 7
                    c = 0
    print_screen(screen)