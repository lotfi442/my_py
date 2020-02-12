from sqlalchemy import create_engine
import pandas as pd
import pymysql
import time

engine = create_engine("mysql+pymysql://root:Mamahabiki3@localhost/simplon")

data = pd.read_sql_query("select * from jeux_video", engine)

print(data)
