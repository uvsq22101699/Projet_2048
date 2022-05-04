#########################################
# groupe MI TD03
# Bertrand Noah
# Wickramasinghe Adipthya Iduwara
# https://github.com/uvsq22101699/Projet_2048
#########################################

import tkinter as tk
from random import *
#from functionNono import process_matrices

racine = tk.Tk()
racine.title("2048")

#################################
# Variables
HAUTEUR = 600
LARGEUR = 600


#################################
# Fonctions

def plateau_jeu():
    """Cette fonction permet de créer le plateau de jeu et d'y insérer 2 valeurs, soit un 2 soit un 4. Sachant que le 2 a 9 fois plus de chance d'apparaitre que le 4 """
    PLATEAU = [[0 for x in range(4)] for z in range(4)]
    # print(PLATEAU)
    if randint(0, 10) <= 9:
        a = 2
    else:
        a = 4
    if randint(0, 10) <= 9:
        b = 2
    else:
        b = 4

    k = randint(0, 3)
    p = randint(0, 3)
    PLATEAU[k][p] = a
    alea = [randint(0, 3), randint(0, 3)]
    while k == alea[0] and p == alea[1]: alea = [randint(0, 3), randint(0, 3)]
    PLATEAU[alea[0]][alea[1]] = b
    return PLATEAU


def affichage_plateau():
    """Cette fonction permet de créer le jeu a proprement parlé, c'est la partie graphique du jeu"""
    largeur_case = LARGEUR // 4
    hauteur_case = HAUTEUR // 4
    for i in range(4):
        for j in range(4):
            if (i + j) % 2 == 0:
                color = "yellow"
            else:
                color = "orange"
            canvas.create_rectangle((i * largeur_case, j * hauteur_case),
                                    ((i + 1) * largeur_case, (j + 1) * hauteur_case), fill=color)


def affichage_valeurs(liste):
    """Cette fonction permet de faire apparaitre le chiffre sur le plateau"""

    largeur_case = LARGEUR // 4
    hauteur_case = HAUTEUR // 4
    emplacement_x = largeur_case // 2
    emplacement_y = hauteur_case // 2
    for a in range(len(liste)):
        for b in range(len(liste[a])):
            if liste[a][b] != 0:
                # print(liste[a][b])
                canvas.create_text(emplacement_x, emplacement_y, fill="red", text=liste[a][b],
                                   font=("Purisa", 150 // 4))
            emplacement_x += hauteur_case
        emplacement_y += largeur_case
        emplacement_x = hauteur_case // 2


def separate_coordinate(coordinate_list):
    " renvoie le résultat final, cela effectue un déplacement vers la droite"
    list_coordinate = [[], [], [], []]
    final_list = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for i in coordinate_list: list_coordinate[i[2]].append([i[0], i[1]])
    coordinate_compressed = []
    for i in list_coordinate: coordinate_compressed.append(coordinate_adder(i))
    for i in range(4):
        for number in coordinate_compressed[i]: final_list[i][number[1]] = number[0]
    return final_list


def coordinate_adder(coordinate):
    " récupere les valeur ainsi que leur position, et ressort les sommes de décalage vers la droite ligne par ligne"
    final_coordinate = []
    for coordinate_index in range(len(coordinate)):
        if coordinate_index != len(coordinate)-1:
            if coordinate[coordinate_index][0] == coordinate[coordinate_index + 1][0]:
                if final_coordinate:
                    if final_coordinate[-1][1] != coordinate_index: 
                        temp = [coordinate[coordinate_index][0] + coordinate[coordinate_index + 1][0], coordinate[coordinate_index + 1][1]]
                else: 
                    temp = [coordinate[coordinate_index][0] + coordinate[coordinate_index + 1][0], coordinate[coordinate_index + 1][1]]
            else: 
                temp = [coordinate[coordinate_index][0], coordinate[coordinate_index][1]]
        else: 
            temp = [coordinate[coordinate_index][0], coordinate[coordinate_index][1]]
        if temp: final_coordinate.append(temp)

    # Cleaning Part
    toClean = []
    for coo in range(len(final_coordinate)):
        if coo != len(final_coordinate)-1:
            if final_coordinate[coo][1] == final_coordinate[coo+1][1]:
                toClean.append(final_coordinate[coo+1])
    for i in toClean:
        final_coordinate.remove(i)

    # Movement part
    if final_coordinate:
        if final_coordinate[-1][1] != 3: final_coordinate[-1][1] = 3
        for coo in range(len(final_coordinate)):
            if final_coordinate[-coo-1][1] != 3 and -coo != 0: final_coordinate[-coo - 1][1] = final_coordinate[-coo][1] - 1
    return final_coordinate


def get_coordinate(liste):
    "Cette fonction renvoie une liste des cases ayant des valeurs avec leur coordonnées "
    coordinate = []
    for i in range(4):
        for number in range(4):
            if liste[i][number] != 0: coordinate.append([liste[i][number], number, i])
    return coordinate


def process_matrices(matrices):
    return separate_coordinate(get_coordinate(matrices))


def rotation_90(matrices):
    " permet d'effectuer une rotation de 90° vers la droite"
    C = []
    for i in range(4):
        l = []
        for j in range(4):
            l.append(matrices[j][i])
        l.reverse()
        C.append(l)
    matrices = C
    return matrices


def move_matrices(matrices, direction):
    global liste
    if direction == "Right":
        liste = process_matrices(matrices)
    elif direction == "Left":
        liste = rotation_90(rotation_90(process_matrices(rotation_90(rotation_90(matrices)))))
    elif direction == "Up":
        liste = rotation_90(rotation_90(rotation_90(process_matrices(rotation_90(matrices)))))
    elif direction == "Down":
        liste = rotation_90(process_matrices(rotation_90(rotation_90(rotation_90(matrices)))))
    affichage_plateau()
    affichage_valeurs(liste)
    ajout_tuile(liste)
    gagner(liste)
    return liste


def ajout_tuile(liste):
    """Cette fonction permet de rajouter une tuile une fois tous les déplacements effectués"""
    print("avant modif liste : ", liste)
    if randint(0, 10) <= 9:
        a = 2
    else:
        a = 4
    liste_tampon = []
    for i in range(4):
        for j in range(4):
            if liste[i][j] == 0:
                liste_tampon += [[i, j]]
    b = randint(0, len(liste_tampon))
    print(liste_tampon[b-1])
    liste[liste_tampon[b-1][0]][liste_tampon[b-1][1]] = a
    print("apres modif liste : ", liste)
    affichage_plateau()
    affichage_valeurs(liste)
    return liste


def Exit(liste):
    a = 0
    for i in range(4):
        for j in range(4):
            a += liste[i][j]
    canvas = tk.Canvas(racine, height=HAUTEUR, width=LARGEUR)
    canvas.grid(column=0, row=0, columnspan=5, rowspan=3)
    canvas.create_text(200, 200, fill="black", text="votre score est : ", font=("Purisa", 50))
    canvas.create_text(300, 300, fill="black", text=str(a), font=("Purisa", 50))


def Save(liste):
    """Cette fonction permet d'enregistrer le plateau de jeu dans un fichier texte"""
    a = liste
    sauvegarde = open("2048_game.txt", "w+")
    sauvegarde.write(str(a))
    sauvegarde.close()


def Charger():
    """Cette fonction permet de charger une partie au format texte, (ne marche pas)"""
    sauvegarde = open("2048_game.txt", "r")
    chargement = sauvegarde.read()
    print(chargement)
    LISTE = chargement
    return LISTE


def gagner(liste):
    for i in range(4):
        for j in range(4):
            if (liste[i][j] == 2048):
                canvas = tk.Canvas(racine, height=HAUTEUR, width=LARGEUR)
                canvas.grid(column=0, row=0, columnspan=5, rowspan=3)
                canvas.create_text(300, 300, fill="black", text="Vous avez Gagnez", font=("Purisa", 50))


def move(event):
    global liste
    touche = event.keysym
    possibleButton = ["Right", "Left", "Up", "Down"]
    if touche in possibleButton:
        move_matrices(liste, touche)
    if touche == "Escape":
        Exit(liste)


bouton = tk.Button(racine, text="quitter", fg="black", command=racine.quit, activebackground="blue", borderwidth=2,
                   bg="green")
bouton.grid(column=1, row=3)

canvas = tk.Canvas(racine, height=HAUTEUR, width=LARGEUR)
canvas.grid(column=1, row=1)

liste = plateau_jeu()
affichage_plateau()
affichage_valeurs(liste)
print(rotation_90(liste))

bouton = tk.Button(racine, text="Sauvegarder", fg="black", command=lambda: Save(liste), activebackground="blue",
                   borderwidth=2, bg="green")
bouton.grid(column=0, row=3)

bouton = tk.Button(racine, text="Charger", fg="black", command=lambda: affichage_valeurs(Charger()),
                   activebackground="blue", borderwidth=2, bg="green")
bouton.grid(column=3, row=3)

racine.bind('<Key>', move)

racine.mainloop()

