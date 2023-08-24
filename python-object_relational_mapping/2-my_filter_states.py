# The module filters states by user input. Takes args from the system and prints matching values from the db
import MySQLdb
import sys

if __name__ == "__main__":

    username, password, dbname, search_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=dbname)

    cursor = db.cursor()

    query = "SELECT * FROM states WHERE name LIKE %s ORDER BY states.id ASC"
    search_pattern = f"{search_name}"

    cursor.execute(query, (search_pattern,))

    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()
