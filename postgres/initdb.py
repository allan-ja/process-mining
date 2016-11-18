
import psycopg2
import psycopg2.extras

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

def 
### MAIN ###

try:
    conn = psycopg2.connect("dbname='mydb' user='allanj' host='localhost' password=''")
except:
    print ("I am unable to connect to the database")


printdb()
namedict =({"id":3, "firstname":"Francis"},
            {"id":4, "firstname":"Dali"},
            {"id":5, "firstname":"Odette"},)

cur = conn.cursor()
cur.executemany("""INSERT INTO Persons(id,firstname) VALUES (%(id)s, %(firstname)s)""", namedict)

printdb()
#conn.commit()
cur.close()
conn.close()
