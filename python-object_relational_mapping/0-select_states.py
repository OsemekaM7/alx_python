import MySQLdb
import sys

if __name__ == "__main__":
    username, password, dbname = sys.argv[1], sys.argv[2], sys.argv[3]
    
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=dbname)
    
    cursor = db.cursor()
    
    query = "SELECT * FROM states ORDER BY states.id ASC"
    cursor.execute(query)

    states = cursor.fetchall()
    
    for state in states:
        print(state)
        
    cursor.close()
    db.close()
