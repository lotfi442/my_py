class superstring :
    def __init__(self, chaine):
        self.ch = chaine
    def capsdown(self):
        self.ch = self.ch.lower()
    def tri(self):
        self.ch = self.ch.split(' ')
        self.ch = sorted(self.ch)
        self.ch = ' '.join(self.ch)
    def ajoute(self, char):
        self.ch += char
    def insert(selfself, char, i):
        self.ch = self.ch[:i] + char + self.ch[i:]
    def upper(self):
        self.ch = self.ch.upper()
    def __str__(self):
        return self.ch


s1 = superstring("boujour tout le monde")
s1.tri()
print(s1)


class formulaire:
    def __init__(self, nom, prenom, anneeNaissance):
        self.nom = nom.upper()
        self.prenom = prenom
        self.anneeNaissance = anneeNaissance

    def age(self):
        return 2020 - self.anneeNaissance

    def majeur(self):
        return self.age() >= 18

    def memeFamille(self, formulaire):
        return self.nom == formulaire.nom

    def memePersonne(self, formulaire):
        return self.nom == formulaire.nom and self.prenom == formulaire.prenom and self.anneeNaissance == formulaire.anneeNaissance

    def __str__(self):  # def __repr__(self):
        return '(' + self.nom + ', ' + self.prenom + ', %s)' % (self.anneeNaissance)


jd = formulaire('Doe', 'John', 2005)
ad = formulaire('Doe', 'Alice', 2000)
sn = formulaire('Nasr', 'Sabine', 1992)
kb = formulaire('Bryant', 'Kobe', 1978)
so = formulaire("O'neal", 'Shaquille', 1972)
ld = formulaire('David', 'Larry', 1947)
jh = formulaire('Hendrix', 'Jimi', 1942)

# print(jd.majeur())
# print(ad.majeur())
# print(jd.memeFamille(ad))
# print(jd, ad)
# rint(ad)

liste_formulaire = []
liste_formulaire.append(jd)
liste_formulaire.append(ad)
liste_formulaire.append(sn)
liste_formulaire.append(kb)
liste_formulaire.append(so)
liste_formulaire.append(ld)
liste_formulaire.append(jh)

a = sorted(liste_formulaire, key=lambda year: year.anneeNaissance)

for i in a:
    print(i)

    # print(sorted(liste_formulaire, key = lambda year : year.anneeNaissance))


class formulaire:
    def init(self, nom, prenom, anneeNaissance):
        self.nom = nom.upper()
        self.prenom = prenom.upper()
        self.anneeNaissance = anneeNaissance

    def age(self):
        return 2020 - self.anneeNaissance

    def majeur(self):
        return self.age() >= 18

    def memeFamille(self, formulaire):
        return self.nom == formulaire.nom

    def str(self):  # la fonction spéciale str comporte en retour nom + prnom + str() pour la voire comme string
        return self.nom + ',' + self.prenom + ',' + str(self.anneeNaissance)


jd = formulaire('Doe', 'John', 2005)
ad = formulaire('doe', 'Alice', 2000)
hm = formulaire('hachem', 'mosbah', 1983)
fr = [jd, ad, hm]  # créer une liste qui comporte les trois listes précedentes

print(jd.majeur())
print(ad.majeur())
print(jd.memeFamille(ad))

# on appelle la fonction sorted (key=lambda) pour prendre un objet précis
fr = sorted(fr, key=lambda x: x.anneeNaissance)
for i in fr:  # boucle pour tous i dans la liste fr
    print(i)  # en sortie i
