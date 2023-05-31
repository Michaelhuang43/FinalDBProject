import mysql.connector as mc
conn = mc.connect(host='localhost', user='root', password='Mushroom123!', database="menagerie")
c = conn.cursor()

query = """
SELECT owner, COUNT(*) as num_pets
FROM pet
GROUP BY owner
"""
c.execute(query)

rows = c.fetchall()

print("Number of pets per owner:")
for row in rows:
    owner = row[0]
    num_pets = row[1]
    print(f"{owner}: {num_pets} pet(s)")

c.close()
conn.close()