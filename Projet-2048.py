#########################################
# groupe MI TD03
# Bertrand Noah 
# Wickramasinghe Adipthya Iduwara
# https://github.com/uvsq22101699/Projet_2048
#########################################

import tkinter as tk
from random import *
#from time import *

racine = tk.Tk()
racine.title("2048")

#################################
#Variables
HAUTEUR = 600
LARGEUR = 600

def plateau_jeu():
    
    PLATEAU = [[1 for a in range(4)]for b in range(4)]
    return PLATEAU
    
def affichage_plateau():
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
    
    largeur_case = LARGEUR // 4
    hauteur_case = HAUTEUR // 4
    emplacement_x = largeur_case // 2
    emplacement_y = hauteur_case // 2
    for a in liste:
        for b in a:
            if str(b) != "0":
                canvas.create_text(emplacement_x, emplacement_y, fill = "red", text = str(b), font=("Purisa", 150//4))
                emplacement_x += largeur_case 
        emplacement_x = largeur_case // 2
        emplacement_y += hauteur_case 

bouton = tk.Button(racine, text = "quitter", fg = "black", command = racine.quit, activebackground = "blue", borderwidth=2, bg = "green")
bouton.grid(column = 1, row = 3)

canvas = tk.Canvas(racine, height = HAUTEUR, width = LARGEUR)
canvas.grid(column = 1, row = 1)

affichage_plateau()
affichage_valeurs(plateau_jeu())

racine.mainloop()