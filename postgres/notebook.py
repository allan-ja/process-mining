
import psycopg2
import psycopg2.extras
import pandas as pd
from sqlalchemy import create_engine

# Functions
def printdb ():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    try:
        cur.execute("""SELECT * from Persons""")
    except:
        print ("I can't SELECT from Persons")

    rows = cur.fetchall()
    print ("\nRows: \n")
    for row in rows:
        print ("   ", row['firstname'])
    return

### MAIN ###

try:
    conn = psycopg2.connect("dbname='mydb' user='allanj' host='localhost' password=''")
except:
    print ("I am unable to connect to the database")

df = pd.read_csv('report_4.csv')

printdb()
namedict ={"id":90, "firstname":"Tom"}

df2 = pd.DataFrame(data=namedict, index=[0])
try:
    engine = create_engine("postgresql://allanj:@localhost/mydb")
    df.to_sql(name='Patients', con=engine, if_exists = 'replace', index=False)
except Exception as e:
    print ("Cannot connect" + str(e))

connection = engine.connect()
result = connection.execute("select * from Persons")
for row in result:
    print("username:", row['firstname'])
connection.close()
#cur = conn.cursor()
#cur.executemany("""INSERT INTO Persons(id,firstname) VALUES (%(id)s, %(firstname)s)""", namedict)

printdb()
#conn.commit()
cur.close()
conn.close()
# -*- coding: utf-8 -*-

