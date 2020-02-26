import pandas as pd
#Utiliser la méthode Series.values_count() 
#pour afficher le décompte du nombre de réponses pour chacune des modalités de la colonnes 
#« Do you celebrate Thanksgiving?
data = pd.read_csv("/Users/lotfi/thanksgiving.csv", encoding = "latin-1")
print(data)
print(data.head())
print(data.columns)
print(data["Do you celebrate Thanksgiving?"].value_counts())
##Filtrer et garder toute les ligne du dataframe pour lesquelles la 
##réponse à la question « Do you celebrate Thanksgiving? » est « Yes ».
print(data.loc[data["Do you celebrate Thanksgiving?"]=="Yes",:])
##Assigner ce nouveau dataframe à data et affiché le.
data = data.loc[data['Do you celebrate Thanksgiving?']=="Yes",:]
print(data[data['Do you celebrate Thanksgiving?']=="Yes"])
##Utiliser la méthode Series.values_count() pour afficher combien de fois 
##chaque résultats apparait pour la question « What is typically the main 
##dish at your Thanksgiving dinner? »
print(data["What is typically the main dish at your Thanksgiving dinner?"].value_counts())
#Afficher la colonne « Do you typically have gravy? » pour les ligne du dataframe data pour 
#lesquelles la colonne « What is typically the main dish at your Thanksgiving dinner? » vaut 
#« Tofurkey » pour la dinde de tofu.
print(data.loc[data["what is typically the main dish at your Thanksgiving dinner?"]=="Tofurkey",:])
#Créer un objet Series indiquant avec des booléens les valeurs de la colonnes 
#« Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. 
#- Apple » qui sont nulles.
#Assigner le résultat à la variable « apple_isnull"])
apple_isnull = pd.isnull(data["Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Apple"])

print(apple_isnull)

#Créer un objet Series indiquant avec des booléens les valeurs de la colonnes « Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pumpkin » qui sont nulles.
#Assigner le résultat à la variable « pumpkin_isnull ».

pumpkin_isnull = pd.isnull(data["Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - pumpkin"])

print(pumpkin_isnull)

#Créer un objet Series indiquant avec des booléens les valeurs de la colonnes 
#« Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. 
#- Pecan » qui sont nulles.
#Assigner le résultat à la variable « pecan_isnull ».

pumpkin_isnull = pd.isnull(data["Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - pecan"])

print(pecan_isnull)

#Combiner les trois objets Series avec l’operateur « & » et 
#assigné le résultat à la variable « pies ».
pies = apple_isnull & pumpkin_isnull & pecan_isnull
print(pies)

##Afficher les valeurs unique et combien de fois elle apparaissent dans la colonnes de pies.
print(pies.value_counts()) 

#Ecrire une fonction qui converti une chaîne de caractère en une valeur entière. 
#Cela permettra de convertir les valeurs de la colonne « Age » en entiers. 
#Cette fonction prendra en paramètre une chaîne de caractères (les valeurs actuelles de la colonne « Age »)

def is_null(str):
	if pd.isnull(str):
		return none
	l = str.split(' ')
	l = [0]
	l = l.replace("+", "")
	l = int(l)

	return l

	#Utiliser la méthode Series.apply() pour appliquer la fonction à chaque valeur de la colonne
	# ‘Age’ du dataframe data.

	int_age = data["age"].apply(is_null)
	print(int_age)

	#Appeler la méthode Series.describe() sur la colonne « int_age » du
#dataframe data et afficher le résultat.
print(int_age.describe())

#Ecrire une fonction pour convertir les revenus en valeur unique de format entier.
def is_null(str):
	if pd.isnull(str):
		return none
	l = str.split(' ')
	l = l[0]
	if prefer:
		return none
	l = l.replace("$", "")
	l = l.replace(",", "")
	l = int(l)
	return l
#Appeler la méthode Series.describe() à la colonne int_income du dataframe data et afficher le résultat.
int_income = data["How much total combined money did all members of your HOUSEHOLD earn last year?"].apply(is_null)

	print(int_income.describe())

#Regarder de quel manière les personnages gagnant moins de 150 000 dollars voyagent.
print(int_income < 150000)
print(personnage)

travel = (data["How far will you travel for Thanksgiving"]) < 150000
print(travel)

print(personnage["how far will you travel for thanksgiving?"].value_counts())

#Faire de même avec les personnages gagnant plus de 150 000 dollars.

personnage1 = data[data["int_income"]] > 150000
print(personnage1["How far will you travel for Thanksgiving?"].value_counts())

#Générer un pivot de table montrant la moyenne d’âge des sondés pour chaque catégorie 
#des questions « Have you ever tried to meet up with hometown friends on Thanksgiving night? » 
#et « Have you ever attended a "Friendsgiving?" ». 

print(data.pivot_table(index = ['Have you ever tried to meet up with hometown friends on Thanksgiving night?'], 
	columns = ['Have you ever attended a "Friendsgiving?"'], values=['int_age'], aggfunc=pd.Series.mean))

#Faire de même avec les revenus avec ces deux questions

print(data.pivot_table(index = ['Have you ever tried to meet up with hometown friends on Thanksgiving night?'], 
columns = ['Have you ever attended a "Friendsgiving?"'], values=['int_income'], aggfunc=pd.Series.mean))


