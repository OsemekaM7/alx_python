import MySQLdb
import sys

if __name__ == "__main__":
    username, password, dbname = sys.argv[1], sys.argv[2], sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=dbname)

    cursor = db.cursor()

    query = "SELECT * FROM cities ORDER BY cities.id ASC"

    cursor.execute(query)

    cities = cursor.fetchall()

    for city in cities:
        print(city)

    cursor.close()
    db.close()
