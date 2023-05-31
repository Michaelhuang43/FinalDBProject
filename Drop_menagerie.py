import mysql.connector as mc
conn = mc.connect(host='localhost', user='root', password='Mushroom123!', database="menagerie")
c = conn.cursor()


def dropdb():
    c.execute("Describe pet")

    for row in c:
        print(row)

def main():
    dropdb()


if __name__ == '__main__':
    main()