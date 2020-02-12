from re import findall
##Question 1
s = "c'est Bien"
l1 = findall('[A-Z][a-z]+', s)
print(l1)

def handscape()
s = "Il Fera Beau Demain"
l1 = findall('[A-Z][a-z]+', s)
l2 = l1[0]
l3 = s.split()
print(l3)
print (l1)
print (l2)
print(l3)


s = "Onze ans déjà que cela passe vite Vous "
s += "vous étiez servis simplement de vos armes la "
s += "mort n'éblouit pas les yeux des partisans Vous "
s += "aviez vos portraits sur les murs de nos villes"

l1 = findall('[A-Z][a-z]+', s)
print(l1)

def hascaps(s):
    l3 = []
    l2 = s.split() # créer une liste
    for i in l2: # boucle
        if ord(i[0]) in range(65,91): # condition
            l3.append(i) # ajoute dans la liste l3
    return l3 # on retourne la liste l3
print(hascap(s))

##Question 2
s = 'Le prix est de 27 euros'
s1 = s.split()
for i, s in enumerate(s1):
    print(i,s)

s = "Le prix est de 27 euro"
z = "je suis ton père"
def inflation(s):
    s1 = s.split()
    for i, n in enumerate(s1):
        if n.isnumeric():
            s1[i] = int(n)*2
            s1[i] = str(s1[i])
        s1 = " ".join(s1)
        return s1

    print(inflation(s))
    print(inflation(z))

    ##Question 3
def ligne(s) :
	y=['']
	x=s.split()

	for i in x:
		i+=" "

		if len(y[-1])+len(i)<=24:
			y[-1]+=i

		else:
			y.append(i)
		return y

	print(ligne(s))

	##Question 4
	import re
	
	def nombre():
		a= re.findall('[\-]?[0-9][\.,,]?[0-9]*','les 3,0 maqueraux valent 6.50')
			print(a)
nombre()






