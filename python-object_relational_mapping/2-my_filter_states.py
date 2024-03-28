#!/usr/bin/python3
# this scrit filters the states in db

import sys
import MySQLdb

def search_states(username, password, db_name, state_name):
    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         passwd=password,
                         db=db_name)

    # Create a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

    try:
        # Execute the SQL command
        cursor.execute(query, (state_name,))
        # Fetch all the rows in a list of lists
        results = cursor.fetchall()
        # Display results
        for row in results:
            print(row)
    except Exception as e:
        print("Error: unable to fetch data")
        print(e)

    # Disconnect from server
    db.close()

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database_name> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    search_states(username, password, db_name, state_name)