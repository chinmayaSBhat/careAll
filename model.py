import sqlite3
conn=sqlite3.connect("db1.db")
cur=conn.cursor()

#Old age person table
cur.execute("""CREATE TABLE IF NOT EXISTS OLD(ID INTEGER PRIMARY KEY AUTOINCREMENT,
NAME VARCHAR(30) NOT NULL,
AGE INT, 
ADDRESS VARCHAR(50),
FUND INT)""")

#youngster table
cur.execute("""CREATE TABLE IF NOT EXISTS YOUNG(ID INTEGER PRIMARY KEY,
NAME VARCHAR(30) NOT NULL,
AGE INT, 
ADDRESS VARCHAR(50))""")

#request approve table
cur.execute("""CREATE TABLE IF NOT EXISTS REQUEST_APPROVE(OID REFERENCES OLD(ID), YID REFERENCES YOUNG(ID),REQUEST INTEGER)""")

# caregving info
cur.execute("""CREATE TABLE IF NOT EXISTS CARE(OID REFERENCES OLD(ID), YID REFERENCES YOUNG(ID))""")

#feedback and rating for oldies
cur.execute("""CREATE TABLE IF NOT EXISTS Y_FEEDBACK(OID REFERENCES OLD(ID),YID REFERENCES YOUNG(ID), FEEDBACK TEXT, RATING INT)""")

#feedback and rating for young
cur.execute("""CREATE TABLE IF NOT EXISTS O_FEEDBACK(YID REFERENCES YOUNG(ID),OID REFERENCES OLD(ID), FEEDBACK TEXT, RATING INT)""")

conn.commit()
