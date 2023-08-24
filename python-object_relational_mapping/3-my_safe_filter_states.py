import MySQLdb
import sys

if __name__ == "__main__":
    # Take arguments from the command line
    username, password, dbname, search_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    
    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=dbname)
    
    # Create a cursor object
    cursor = db.cursor()
    
    # Prepare the SQL query using parameterized query
    query = "SELECT * FROM states WHERE name LIKE %s ORDER BY states.id ASC"
    search_pattern = f"{search_name}%"  # Adding '%' for pattern matching
    
    # Execute the parameterized query
    cursor.execute(query, (search_pattern,))
    
    # Fetch all the rows
    states = cursor.fetchall()
    
    # Display the results
    for state in states:
        print(state)
    
    # Close the cursor and the database connection
    cursor.close()
    db.close()
