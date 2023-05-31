import mysql.connector as mc
conn = mc.connect(host='localhost', user='root', password='Mushroom123!', database="menagerie")
c = conn.cursor()

query = "SELECT * FROM PET"
c.execute(query)
columns = c.fetchall()
for column in columns:
        print(column)
c.close()

conn.close()