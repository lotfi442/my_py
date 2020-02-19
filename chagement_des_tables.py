from sqlalchemy import create_engine
import pandas as pd
from re import findall


engine = create_engine("mysql+pymysql://user:lotfi.baya@localhost/base")

def chargement(link, table, names_elus):
    print("Lecture des données")
    link = '/Users/lotfi/Documents/git/Evaluation/Tables/nom_de_table'
    df = pd.read_excel(link , skiprows=0,header=1, set='\t', names = names)
    df.to_sql('name', con = engine, if_exists='append', index = False)
    return print("fin")

chargement('/Users/lotfi/Documents/git/Evaluation/Tables/nom_de_table', 'elus', names_elus)

##voici le  code pour alimenter une base de donnée a appliquer pour chaque table choisie .
##Les fichier excell ont été perdu donc leur titre n'apparaitron pas dans le code. 