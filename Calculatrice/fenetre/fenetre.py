from tkinter import *
from tkinter import ttk
from boutonCommandes import (commandeNombre, commandeOperation, commandeEgal, commandeSup, commandeC, commandeCe,
                             commandeVirgule)


class Fenetre:

    def __init__(self, nom=""):
        memoireCalcul = []

        fenetre = Tk()
        fenetre.title(nom)
        fenetre.geometry("368x572")

        affichageEcran = Canvas(fenetre, width=368, height=150)
        affichageEcran.create_rectangle(0, 0, 400, 150, fill="lightgray")
        affichageEcran.grid(row=0, column=0, rowspan=2, columnspan=100)

        separateurParenthese = Canvas(fenetre, width=90, height=69)
        separateurParenthese.create_rectangle(0, 0, 90, 69)
        separateurParenthese.grid(row=2, column=0, columnspan=2)

        zoneTexte = Label(fenetre, text="", font=("Arial", 15))
        zoneTexte.grid(row=1, column=3)
        zoneHistoriqueCalcul = Label(fenetre, text="", font=("Arial", 13))
        zoneHistoriqueCalcul.grid(row=0, column=1)

        ligne1 = 2
        ligne2 = 3
        ligne3 = 4
        ligne4 = 5
        ligne5 = 6
        ligne6 = 7
        colonne1 = 1
        colonne2 = 2
        colonne3 = 3
        colonne4 = 4

        bouton1 = Bouton(fenetre, ligne3, colonne1, "1", lambda: commandeNombre("1", zoneTexte))
        bouton2 = Bouton(fenetre, ligne3, colonne2, "2", lambda: commandeNombre("2", zoneTexte))
        bouton3 = Bouton(fenetre, ligne3, colonne3, "3", lambda: commandeNombre("3", zoneTexte))
        bouton4 = Bouton(fenetre, ligne4, colonne1, "4", lambda: commandeNombre("4", zoneTexte))
        bouton5 = Bouton(fenetre, ligne4, colonne2, "5", lambda: commandeNombre("5", zoneTexte))
        bouton6 = Bouton(fenetre, ligne4, colonne3, "6", lambda: commandeNombre("6", zoneTexte))
        bouton7 = Bouton(fenetre, ligne5, colonne1, "7", lambda: commandeNombre("7", zoneTexte))
        bouton8 = Bouton(fenetre, ligne5, colonne2, "8", lambda: commandeNombre("8", zoneTexte))
        bouton9 = Bouton(fenetre, ligne5, colonne3, "9", lambda: commandeNombre("9", zoneTexte))
        bouton0 = Bouton(fenetre, ligne6, colonne2, "0", lambda: commandeNombre("0", zoneTexte))

        boutonDivision = Bouton(fenetre, ligne2, colonne4, "/", lambda: commandeOperation("/", zoneTexte, memoireCalcul, zoneHistoriqueCalcul))
        boutonMultiplication = Bouton(fenetre, ligne3, colonne4, "X", lambda: commandeOperation("X", zoneTexte, memoireCalcul, zoneHistoriqueCalcul))
        boutonPlus = Bouton(fenetre, ligne4, colonne4, "+", lambda: commandeOperation("+", zoneTexte, memoireCalcul, zoneHistoriqueCalcul))
        boutonMoins = Bouton(fenetre, ligne5, colonne4, "-", lambda: commandeOperation("-", zoneTexte, memoireCalcul, zoneHistoriqueCalcul))

        boutonEgal = Bouton(fenetre, ligne6, colonne4, "=", lambda: commandeEgal(zoneTexte,zoneHistoriqueCalcul, memoireCalcul), "green")

        boutonVirgule = Bouton(fenetre, ligne6, colonne3, ",", lambda: commandeVirgule(",", zoneTexte))

        boutonParentheseGauche = Button(separateurParenthese, text="(", padx=0, pady=0, width=3, height=2, font=('Arial', 16), command=lambda: commandeNombre("(", zoneTexte))
        boutonParentheseGauche.grid(row=0, column=1)
        boutonParentheseDroite = Button(separateurParenthese, text=")", padx=0, pady=0, width=3, height=2, font=('Arial', 16), command=lambda: commandeNombre(")", zoneTexte))
        boutonParentheseDroite.grid(row=0, column=2)

        #boutonPourcentage = Bouton(fenetre, ligne1, colonne1, "%", lambda: commandePourcentage(zoneTexte))
        boutonNegative = Bouton(fenetre, ligne6, colonne1, "X(-1)")
        boutonFonctionInverse = Bouton(fenetre, ligne2, colonne1, "1/x")
        boutonCarre = Bouton(fenetre, ligne2, colonne2, "x²")
        boutonRacineCarre = Bouton(fenetre, ligne2, colonne3, "sqrt(x)")

        boutonSup = Bouton(fenetre, ligne1, colonne4, "<-", lambda: commandeSup(zoneTexte, memoireCalcul), "red")
        boutonToutSuprimer = Bouton(fenetre, ligne1, colonne3, "C", lambda: commandeC(zoneTexte, memoireCalcul))
        boutonSuprimerEnCours = Bouton(fenetre, ligne1, colonne2, "CE", lambda: commandeCe(zoneTexte, memoireCalcul, zoneHistoriqueCalcul))

        fenetre.mainloop()


class Bouton:

    def __init__(self, fenetre, ligne, colonne, texte="", commande=None, couleur=None):
        self.fenetre = fenetre
        self.ligne = ligne
        self.colonne = colonne
        self.texte = texte
        self.color = couleur
        DIMENSION_BOUTON = [12, 3, 5, 2]

        (Button(fenetre, text=self.texte, command=commande, padx=DIMENSION_BOUTON[0],
                pady=DIMENSION_BOUTON[1],
                width=DIMENSION_BOUTON[2], height=DIMENSION_BOUTON[3],
                font=('Arial', 16), bg=self.color)
         .grid(row=ligne, column=colonne))
