from sqlalchemy import create_engine
import pandas as pd
import time

engine = create_engine("mysql+pymysql://hachem:tiger@localhost/siret")

def importcsv(link, table):
    print("Lecture des données")
    start_time = time.time()
    df = pd.read_excel(link , skiprows=0,header=1)
    print("Données lu")

    to_sql(table, con = engine, if_exists='replace', index = False)

    return print("Temps d execution : %s secondes ---" % (time.time() - start_time))


importcsv('/Users/mosbahhachem/Documents/git/environnement_dev_data/exercice_python_sql/liste_1993.xls', 'liste_1993')