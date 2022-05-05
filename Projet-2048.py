#########################################
# groupe MI TD03
# Bertrand Noah
# Wickramasinghe Adipthya Iduwara
# https://github.com/uvsq22101699/Projet_2048
#########################################

import tkinter as tk
from random import *
import ast
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
    couleurs = ["#eee4da", "#ede0c8", "#f2b179", "#f59563", "#f67c5f", "#f65e3b", "#edcf72", "#edcc61", "#edc850", "#edc53f", "#edc22e"]
    couleur = "gray"
    canvas.delete()
    for i in range(4):
        for j in range(4):
            if liste[i][j] == 2:
                couleur = couleurs[0]
            elif liste[i][j] == 4:
                couleur = couleurs[1]
            elif liste[i][j] == 8:
                couleur = couleurs[2]
            elif liste[i][j] == 16:
                couleur = couleurs[3]
            elif liste[i][j] == 32:
                couleur = couleurs[4]
            elif liste[i][j] == 64:
                couleur = couleurs[5]
            elif liste[i][j] == 128:
                couleur = couleurs[6]
            elif liste[i][j] == 256:
                couleur = couleurs[7]
            elif liste[i][j] == 512:
                couleur = couleurs[8]
            elif liste[i][j] == 1024:
                couleur = couleurs[9]
            elif liste[i][j] == 2048:
                couleur = couleurs[10]
            else:
                couleur = "gray"
            canvas.create_rectangle((j * largeur_case, i * hauteur_case), ((j + 1) * largeur_case, (i + 1) * hauteur_case), fill=couleur)


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
                canvas.create_text(emplacement_x, emplacement_y, fill="black", text=liste[a][b],
                                   font=("Purisa", 150 // 4))
            emplacement_x += hauteur_case
        emplacement_y += largeur_case
        emplacement_x = hauteur_case // 2


def coordinate_adder(liste_fusion):
    " récupere les valeur ainsi que leur position, et ressort les sommes de décalage vers la droite ligne par ligne"
    for i in range(len(liste_fusion)):
        for j in range(len(liste_fusion[i])):
            if liste_fusion[i][1] == 0 and liste_fusion[i][2] == 0 and liste_fusion[i][0] == liste_fusion[i][3]:
                liste_fusion[i][0] += liste_fusion[i][3]
                liste_fusion[i][3] = 0
                break
            if liste_fusion[i][1] == 0 and liste_fusion[i][0] == liste_fusion[i][2]:
                liste_fusion[i][0] += liste_fusion[i][2]
                liste_fusion[i][1] = liste_fusion[i][3]
                liste_fusion[i][2] = 0
                liste_fusion[i][3] = 0
                break
            if liste_fusion[i][2] == 0 and liste_fusion[i][0] == liste_fusion[i][1] == liste_fusion[i][3]:
                liste_fusion[i][0] += liste_fusion[i][1]
                liste_fusion[i][1] = liste_fusion[i][3]
                liste_fusion[i][2] = 0
                liste_fusion[i][3] = 0
                break
            if liste_fusion[i][1] == 0 and liste_fusion[i][0] == liste_fusion[i][2]:
                liste_fusion[i][0] += liste_fusion[i][2]
                liste_fusion[i][1] = liste_fusion[i][3]
                liste_fusion[i][2] = 0
                liste_fusion[i][3] = 0
                break
            if liste_fusion[i][2] == 0 and liste_fusion[i][1] == liste_fusion[i][3]:
                liste_fusion[i][1] += liste_fusion[i][3]
                liste_fusion[i][2] = 0
                liste_fusion[i][3] = 0
                if liste_fusion[i][0] == 0:
                    liste_fusion[i][0] = liste_fusion[i][1]
                    liste_fusion[i][1] = liste_fusion[i][2]
                    liste_fusion[i][2] = 0
                break
            if j < 3:
                if liste_fusion[i][j] == liste_fusion[i][j+1]:
                    liste_fusion[i][j] += liste_fusion[i][j]
                    liste_fusion[i][j+1] = 0
            if j > 0 and liste_fusion[i][j-1] == 0:
                liste_fusion[i][j-1] = liste_fusion[i][j]
                liste_fusion[i][j] = 0
                
        for k in range(len(liste_fusion[i])):
            if liste_fusion[i][k] == 0 and k < 3:
                liste_fusion[i][k] = liste_fusion[i][k+1]
                liste_fusion[i][k+1] = 0
    return liste_fusion


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
    a = []
    for i in range(len(liste)):
        a.append([])
        for j in range(len(liste)):
            a[i].append(liste[i][j])
    if direction == "Right":
        liste = rotation_90(rotation_90(coordinate_adder(rotation_90(rotation_90(matrices)))))
    elif direction == "Left":
        liste = coordinate_adder(matrices)
    elif direction == "Up":
        liste = rotation_90(coordinate_adder(rotation_90(rotation_90(rotation_90(matrices)))))
    elif direction == "Down":
        liste = rotation_90(rotation_90(rotation_90(coordinate_adder(rotation_90(matrices)))))
    affichage_plateau()
    affichage_valeurs(liste)
    if a == rotation_90(rotation_90(coordinate_adder(rotation_90(rotation_90(matrices))))) and a == coordinate_adder(matrices) and a == rotation_90(coordinate_adder(rotation_90(rotation_90(rotation_90(matrices))))) and a == rotation_90(rotation_90(rotation_90(coordinate_adder(rotation_90(matrices))))):
        canvas.create_text(300, 300, fill="black", text="Vous avez perdu", font=("Purisa", 50))
    if a != liste:
        ajout_tuile(liste)
    label["text"] = "Score: " + str(score())
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
    sauvegarde = open("2048_game.txt", "a")
    sauvegarde.write(str(a) + "\n")
    sauvegarde.close()


def Charger():
    """Cette fonction permet de charger une partie au format texte, (ne marche pas)"""
    global liste
    sauvegarde = open("2048_game.txt", "r")
    ligne = int(input("Entrez le numéro de la sauvegarde : "))
    chargement = sauvegarde.readlines()
    chargement = chargement[ligne]
    chargement = ast.literal_eval(chargement)
    liste = chargement
    return liste


def gagner(liste):
    for i in range(4):
        for j in range(4):
            if (liste[i][j] == 2048):
                canvas.create_text(300, 300, fill="black", text="Vous avez gagné", font=("Purisa", 50))


def move(event):
    global liste
    touche = event.keysym
    possibleButton = ["Right", "Left", "Up", "Down"]
    if touche in possibleButton:
        move_matrices(liste, touche)
    if touche == "Escape":
        Exit(liste)


def score():
    score = 0
    for i in range(len(liste)):
        for j in range(len(liste[i])):
            score += liste[i][j]
    return score


bouton = tk.Button(racine, text="quitter", fg="black", command=racine.quit, activebackground="blue", borderwidth=2,
                   bg="green")
bouton.grid(column=1, row=3)

canvas = tk.Canvas(racine, height=HAUTEUR, width=LARGEUR)
canvas.grid(column=1, row=1)

liste = plateau_jeu()
# liste = [[4, 8, 2, 16], [2, 512, 32, 2], [4, 1024, 8, 16], [8, 16, 2, 2]]
affichage_plateau()
affichage_valeurs(liste)
print(rotation_90(liste))

bouton = tk.Button(racine, text="Sauvegarder", fg="black", command=lambda: Save(liste), activebackground="blue",
                   borderwidth=2, bg="green")
bouton.grid(column=0, row=3)

bouton = tk.Button(racine, text="Charger", fg="black", command=lambda: affichage_valeurs(Charger()),
                   activebackground="blue", borderwidth=2, bg="green")
bouton.grid(column=3, row=3)

label = tk.Label(text="Score: " + str(score()))
label.grid(column=0, row=1)

racine.bind('<Key>', move)

racine.mainloop()

