from sqlalchemy import create_engine
import pandas as pd
import pymysql
import time

engine = create_engine("mysql+pymysql://root:Mamahabiki3@localhost/siren")


def importcsv(link, table, date):
    print("Lecture des données")
    start_time = time.time()
    csize = 750000
    df = pd.read_csv(link, compression='zip', chunksize=csize, parse_dates=date, low_memory=FTalse)
    print("Données lu")
    i = csize
    for chunk in df:
        chunk.to_sql(table, con=engine, if_exists='append', index=False)
        i += csize
        print(i)
    return print("Temps d execution : %s secondes ---" % (time.time() - start_time))


importcsv('/Users/lotfi/Documents/projects/my_py/test.py',
          ['dateFin', 'dateDebut'])