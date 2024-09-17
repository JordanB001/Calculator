from errors.exceptions import SymboleSansChiffreAvant, SymboleDouble, VirguleDouble, PourcentageSymbole


def commandeNombre(lettre, label):
    txtLabel = label.cget("text")

    if len(txtLabel) != 0 and txtLabel in ["/", "X", "+", "-"]:
        label.config(text=lettre)
    else:
        label.config(text=txtLabel + lettre)


def commandeOperation(symbole, label, memoireCalcul, zoneHistoriqueCalcul):
    txtLabel = label.cget("text")
    zoneHistoriqueCalcul.config(text=txtLabel)

    if len(txtLabel) == 0:
        raise SymboleSansChiffreAvant
    elif txtLabel[-1] in ["/", "X", "+", "-"]:
        label.config(text="")
        raise SymboleDouble
    else:
        memoireCalcul.append(txtLabel)
        memoireCalcul.append(symbole)
        label.config(text=symbole)


def commandeVirgule(lettre, label):
    txtLabel = label.cget("text")

    if len(txtLabel) != 0:
        if "," in txtLabel:
            raise VirguleDouble
        else:
            label.config(text=txtLabel + lettre)
    else:
        label.config(text="0" + lettre)


def commandeSup(label, memoireCalcul):
    textLabel = label.cget("text")

    if len(textLabel) == 0:
        pass
    elif len(memoireCalcul) == 0:
        textLabel = textLabel[:-1]
        label.config(text=textLabel)
    else:
        textLabel = textLabel[:-1]
        del memoireCalcul[-1]
        del memoireCalcul[-1]
        label.config(text=textLabel)


def commandeC(label, memoireCalcul):
    textLabel = label.cget("text")

    if len(textLabel) == 0:
        pass
    elif len(memoireCalcul) == 0:
        label.config(text="")
    else:
        del memoireCalcul
        label.config(text="")


def commandeCe(label, memoireCalcul, zoneHistorique):
    del memoireCalcul
    label.config(text="")
    zoneHistorique.config(text="")


def commandeEgal(label, histoCalcul, calculMemoire):
    texteLabel = label.cget("text")

    if len(calculMemoire) <= 1:
        return None

    if len(texteLabel) != 0:
        calculMemoire.append(texteLabel)
        histoCalcul.config(text="".join(calculMemoire))

        for chercheVirgule in calculMemoire:
            if "," in chercheVirgule:
                partieEntiere, partieDecimale = chercheVirgule.split(",")
                partieDecimale = float(partieDecimale) / (10 ** len(partieDecimale))
                calculMemoire[calculMemoire.index(chercheVirgule)] = float(partieEntiere) + float(partieDecimale)

        while len(calculMemoire) > 1:

            while "/" in calculMemoire:
                positionDiviser = calculMemoire.index("/")
                calculMemoire[positionDiviser] = float(calculMemoire[positionDiviser - 1]) / float(
                    calculMemoire[positionDiviser + 1])
                del calculMemoire[positionDiviser - 1]
                del calculMemoire[positionDiviser]

            while "X" in calculMemoire:
                positionMultiplier = calculMemoire.index("X")
                calculMemoire[positionMultiplier] = float(calculMemoire[positionMultiplier - 1]) * float(
                    calculMemoire[positionMultiplier + 1])
                del calculMemoire[positionMultiplier - 1]
                del calculMemoire[positionMultiplier]

            while "-" in calculMemoire:
                positionSoustraction = calculMemoire.index("-")
                calculMemoire[positionSoustraction] = float(calculMemoire[positionSoustraction - 1]) - float(
                    calculMemoire[positionSoustraction + 1])
                del calculMemoire[positionSoustraction - 1]
                del calculMemoire[positionSoustraction]

            while "+" in calculMemoire:
                positionAddition = calculMemoire.index("+")
                calculMemoire[positionAddition] = float(calculMemoire[positionAddition - 1]) + float(
                    calculMemoire[positionAddition + 1])
                del calculMemoire[positionAddition - 1]
                del calculMemoire[positionAddition]

        calculMemoire[0] = str(round(calculMemoire[0], 8))
        label.config(text=calculMemoire)
        del calculMemoire[0]


