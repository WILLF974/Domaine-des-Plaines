#coding: utf-8
# utilise les fichiers new.py
# utilise les fichiers newr.py

from tkinter import *

from new import faireApparaitreLeToplevel
fen = Tk()
fen.geometry("400x300")

# import des fichiers externes
# new -> a transformer en nouvel_fiche
from new import faireApparaitreLeToplevel

# 1)  Création de la barre des menu
menu_Bar = Menu(fen)

# 2) Création des menus principaux
menu_Fichier = Menu(menu_Bar)
menu_Edit = Menu(menu_Bar)
menu_BD = Menu(menu_Bar)

# 3) Ajout des menu principaux à la barre des menu
menu_Bar.add_cascade(label = "Fichier", menu = menu_Fichier)
menu_Bar.add_cascade(label = "Edit", menu = menu_Edit)
menu_Bar.add_cascade(label = "Base de données", menu = menu_BD)

# 4) Ajout des commandes aux menu principaux
# Ajout au menu Fichier
menu_Fichier.add_command(label = "Nouveau", command = faireApparaitreLeToplevel)
menu_Fichier.add_command(label = "Ouvrir")
menu_Fichier.add_command(label = "Enregistrer")
menu_Fichier.add_command(label = "Enregistrer sous")
menu_Fichier.add_command(label = "Quitter", command = quit)
# Ajout au menu Base de données
menu_BD.add_command(label = "Nouveau type d'animal")
menu_BD.add_command(label = "Nouvelle race")

fen.config(menu = menu_Bar)

# boucle infinie
fen.mainloop()
