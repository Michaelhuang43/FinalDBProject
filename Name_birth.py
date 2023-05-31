import mysql.connector as mc
conn = mc.connect(host='localhost', user='root', password='Mushroom123!', database="menagerie")
c = conn.cursor()

query = "SELECT name, birth FROM pet"
c.execute(query)
rows = c.fetchall()
for row in rows:
    name = row[0]
    birth = row[1]
    print(f"name: {name}, birth:{birth}")
c.close()
conn.close()