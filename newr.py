# coding:utf-8
# Base "DDP.db" avec TABLE "race" ("idNom", "NomRace" TEXT)
import sqlite3
import tkinter

def sauver_race(*args):
   
    conn = sqlite3.connect("DDP.db")
    cur = conn.cursor()
    # NomRace = "le nom de la race a sauvegarder"
    NomDeRace = var_entry_race.get()
    NewNomDeRace = (cur.lastrowid, NomDeRace)
    print(NomDeRace)
    cur.execute('INSERT INTO race VALUES (?,?)',NewNomDeRace)
    # cur.execute(req, NomDeRace)
    conn.commit()
    conn.close()


fen_race = tkinter.Tk()

# Fenêtre principale
fen_race.geometry("300x200")
fen_race.title("Saisie d'une nouvelle race")

Label_fen_race = tkinter.Label(fen_race, text = "Nom de la race :")
var_entry_race = tkinter.StringVar()
Entry_fen_race = tkinter.Entry(fen_race, width = 30, textvariable = var_entry_race)
sauve_button = tkinter.Button(fen_race, text ="Enregistrer", command = sauver_race)
quitter_button = tkinter.Button(fen_race, text = "Quitter", command = quit)

# Affichage des Widgets
Label_fen_race.pack()
Entry_fen_race.pack()
sauve_button.place(x=50 , y=160)
quitter_button.place(x=150 , y=160)

# Boucle principale
fen_race.mainloop()