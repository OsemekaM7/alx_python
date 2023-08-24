import MySQLdb
import sys

if __name__ == "__main__":
    # Take arguments from the command line
    username, password, dbname, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    
    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=dbname)
    
    # Create a cursor object
    cursor = db.cursor()
    
    # Prepare the SQL query with parameterized query to avoid SQL injection
    query = "SELECT cities.name FROM cities\
             INNER JOIN states ON cities.state_id = states.id\
             WHERE states.name = %s\
             ORDER BY cities.id ASC"
    
    # Execute the SQL query with the state name parameter
    cursor.execute(query, (state_name,))
    
    # Fetch all the rows
    cities = cursor.fetchall()
    
    # Display the results
    for city in cities:
        print(city[0])  # The city name is in the first column
        
    # Close the cursor and the database connection
    cursor.close()
    db.close()
