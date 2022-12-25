from fonctions import *

screen = []


def init_screen(scr, choix_mode):
    if choix_mode == 1:
        lin = 22
        col = 72
    elif choix_mode == 2:
        lin = 7
        col = 25

    for line in range(lin):
        lst = []
        for e in range(col):
            lst.append(0)
        scr.append(lst)


def insert_bloc_screen(scr, bloc, l, c, num):
    for i in range(len(bloc)):
        for j in range(len(bloc[i])):
            pos_x = l + i
            pos_y = c + j
            screen[pos_x][pos_y] = bloc[i][j]
        screen[l + 6][c] = num


def print_screen(scr):
    for i in range(len(scr)):
        for j in range(len(scr[i])):
            if scr[i][j] == 1:
                print("◆ ", end="")
            elif scr[i][j] == 0:
                print("  ", end="")
            else:
                print("{}".format(scr[i][j]), end="")
        print()


def affichage_num(num):
    if num < 11:
        num = " " + str(num)
    return num


def affiche_tout(screen, choix_plateau, choix_mode):
    c = 0
    l = 0
    if choix_plateau == 1:
        if choix_mode == 1:
            for i in triangle_list:
                insert_bloc_screen(screen, bloc_list[i], l, c, str(affichage_num(i)))
                c += 6
                if c == 72:
                    l += 7
                    c = 0
        elif choix_mode == 2:
            rand_list = random.sample(triangle_list, 3)
            for i in range(len(rand_list)):
                insert_bloc_screen(screen, bloc_list[rand_list[i]], l, c, str(rand_list[i]))
                c += 6
    if choix_plateau == 2:
        if choix_mode == 1:
            for i in losange_list:
                insert_bloc_screen(screen, bloc_list[i], l, c, str(affichage_num(i)))
                c += 6
                if c == 72:
                    l += 7
                    c = 0
        elif choix_mode == 2:
            rand_list = random.sample(losange_list, 3)
            for i in range(len(rand_list)):
                insert_bloc_screen(screen, bloc_list[rand_list[i]], l, c, str(rand_list[i]))
                c += 6
    if choix_plateau == 3:
        if choix_mode == 1:
            for i in cercle_list:
                insert_bloc_screen(screen, bloc_list[i], l, c, str(affichage_num(i)))
                c += 6
                if c == 72:
                    l += 7
                    c = 0
        elif choix_mode == 2:
            rand_list = random.sample(cercle_list, 3)
            for i in range(len(rand_list)):
                insert_bloc_screen(screen, bloc_list[rand_list[i]], l, c, str(rand_list[i]))
                c += 6
    print_screen(screen)
