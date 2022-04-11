#########################################
# groupe MI TD03
# Bertrand Noah 
# Wickramasinghe Adipthya Iduwara
# https://github.com/uvsq22101699/Projet_2048
#########################################

import tkinter as tk
from random import *
from time import *

racine = tk.Tk()
racine.title("2048")

#################################
#Variables
HAUTEUR = 600
LARGEUR = 600

def plateau_jeu():
    """Cette fonction permet de créer le plateau de jeu et d'y insérer 2 valeurs, soit un 2 soit un 4. Sachant que le 2 a 9 fois plus de chance d'apparaitre que le 4 """
    PLATEAU = [[0 for x in range(4)]for z in range(4)]
    #print(PLATEAU)
    a = randint(0, 100)
    b = randint(0, 100)
    if a <= 90:     a = 2
    else:           a = 4
    if b <= 90:     b = 2
    else:           b = 4

    k = randint(0, 3)
    p = randint(0, 3)
    PLATEAU[k][p] = a
    k2 = randint(0, 3)
    p2 = randint(0, 3)
    while PLATEAU[k2][p2] == a:
        k2 = randint(0, 3)
        p2 = randint(0, 3)
    
    #print(k2, p2)
    PLATEAU[k2][p2] = b
    return PLATEAU

def affichage_plateau():

    """Cette fonction permet de créer le jeu a proprement parlé, c'est la partie graphique du jeu"""
    largeur_case = LARGEUR // 4
    hauteur_case = HAUTEUR // 4
    for i in range(4):
        for j in range(4):
            if (i+j) % 2 == 0:
                color = "yellow"   
            else:
                color = "orange"
            #TEXT = str(valeur(creation(5, 5)))
            canvas.create_rectangle((i*largeur_case, j*hauteur_case),
                ((i+1)*largeur_case, (j+1)*hauteur_case), fill=color)
            #il faut ajouter du texte pour chaque case

def affichage_valeurs(liste):
    """Cette fonction permet de faire apparaitre le chiffre sur le plateau"""
    
    largeur_case = LARGEUR // 4
    hauteur_case = HAUTEUR // 4
    emplacement_x = largeur_case // 2
    emplacement_y = hauteur_case // 2
    for a in range(len(liste)):
        for b in range(len(liste[a])):
            if liste[a][b] != 0:
                canvas.create_text(emplacement_x, emplacement_y, fill = "red", text = liste[a][b], font=("Purisa", 150//4))
            emplacement_x += hauteur_case
    
        emplacement_y += largeur_case
        emplacement_x = hauteur_case // 2

def bouger_haut(LISTE):
    """Le but de cette fonction est de permettre les déplacements vers le haut, on verifie si la ligne la plus en bas vide
    si elle l est on ne fait rien, si elle ne l est pas on somme toutes ses valeurs a leur voisin du dessus, on repete ce processus pour toutes les lignes"""

    print("avant modif : ", LISTE)
    for T in range(3):
        if LISTE[3-T] != [0, 0, 0, 0]:
            for i in range(4):
                if (LISTE[2-T][i] == LISTE[3-T][i]) or (LISTE[2-T][i] == 0) :
                    LISTE[2-T][i] += LISTE[3-T][i]
                    LISTE[3-T][i] = 0
                
    print("modifié : ", LISTE)
    canvas.after(20)
    affichage_plateau()
    affichage_valeurs(LISTE)
    return LISTE

def bouger_bas(LISTE):
    """Le but de cette fonction est de permettre les déplacements vers le bas, on verifie si la ligne la plus en haut est vide
    si elle l est on ne fait rien, si elle ne l est pas on somme toutes ses valeurs a leur voisin du dessous, on repete ce processus pour toutes les lignes"""

    print("avant modif : ", LISTE)
    for T in range(3):
        if LISTE[T] != [0, 0, 0, 0]:
            for i in range(4):
                if (LISTE[T+1][i] == LISTE[T][i]) or (LISTE[T+1][i] == 0) :
                    LISTE[T+1][i] += LISTE[T][i]
                    LISTE[T][i] = 0
                
    print("modifié : ", LISTE)
    #canvas.after(20)
    affichage_plateau()
    affichage_valeurs(LISTE)
    return LISTE

def bouger_droite(LISTE):
    """Le but de cette fonction est de permettre les déplacements vers la droite, on verifie si la ligne la plus en haut est vide
    si elle l est on ne fait rien, si elle ne l est pas on somme toutes ses valeurs a leur voisin de droite, on repete ce processus pour toutes les lignes"""


    print("avant modif : ", LISTE)
    for T in range(4):
        if LISTE[T] != [0, 0, 0, 0]:
            for i in range(3):
                if (LISTE[T][i+1] == LISTE[T][i]) or (LISTE[T][i+1] == 0) :
                    LISTE[T][i+1] += LISTE[T][i]
                    LISTE[T][i] = 0
    print("modifié : ", LISTE)
    #canvas.after(20)
    affichage_plateau()
    affichage_valeurs(LISTE)
    return LISTE

def bouger_gauche(LISTE):
    """Le but de cette fonction est de permettre les déplacements vers la gauche, elle s'appuie sur la fonction bouger_droite car bouger vers la droite puis 
    renverser chaque sous-liste est équivalent à a faire un déplacement vers la gauche"""

    #print(LISTE)
    #bouger_droite(LISTE)
    for i in range(len(LISTE)):
        LISTE[i].reverse()
        if i == len(LISTE)-1:
            bouger_droite(LISTE)
            LISTE.reverse()
    #print("modifié : ", LISTE)
    #canvas.after(20)
    """affichage_plateau()
    affichage_valeurs(LISTE)"""
    return LISTE

def ajout_tuile(LISTE):
    print("avant modif liste : ", LISTE)
    a = randint(0, 100)
    if a <= 90:     a = 2
    else:           a = 4
    liste_tampon = []
    for i in range(4):
        for j in range(4):
            if LISTE[i][j] == 0:
                liste_tampon += [[i, j]]
    b = randint(0, len(liste_tampon))
    print(liste_tampon[b])
    LISTE[liste_tampon[b][0]][liste_tampon[b][1]] = a
    print("apres modif liste : ", LISTE)
    affichage_plateau()
    affichage_valeurs(LISTE)
    return LISTE

def move(event):
    global LISTE
    touche =event.keysym
    if touche == "Right":
        bouger_droite(LISTE)
        ajout_tuile(LISTE)
    if touche == "Left":
        bouger_gauche(LISTE)
        ajout_tuile(LISTE)
    if touche == "Up":
        bouger_haut(LISTE)
        ajout_tuile(LISTE)
    if touche == "Down":
        bouger_bas(LISTE)
        ajout_tuile(LISTE)

"""def gagner(LISTE): 

    for i in range(4): 
        for j in range(4): 
            if(LISTE[i][j]== 2048): 
                return "Gagné"
            if LISTE[i][j] == 0:
                pass"""

bouton = tk.Button(racine, text = "quitter", fg = "black", command = racine.quit, activebackground = "blue", borderwidth=2, bg = "green")
bouton.grid(column = 1, row = 3)

canvas = tk.Canvas(racine, height = HAUTEUR, width = LARGEUR)
canvas.grid(column = 1, row = 1)

LISTE = plateau_jeu()
affichage_plateau()
affichage_valeurs(LISTE)
#print(bouger_haut(tableau))
#canvas.bind("<Up>", bouger_haut(tableau))
#canvas.bind("<Up>", bouger_haut(tableau))

racine.bind('<Key>',move)

racine.mainloop()
