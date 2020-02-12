

class Carte:
    def __init__(self, couleur = 0, valeur = 2):
        self.couleur = couleur
        self.valeur = valeur
        noms_couleurs = ['trèfle', 'carreau', 'cœur', 'pique']
        noms_valeurs = [None, 'as', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'valet', 'dame', 'roi']

    def __str__(self):
        return '%s de %s' % (Carte.noms_valeurs[self.valeur], Carte.noms_couleurs[self.couleur])

carte1 = Carte(2, 11)
print(carte1)


def plusGrandQue(self, other):
    t1 = self.couleur, self.valeur
    t2 = other.couleur, other.valeur
    return t1 < t2

