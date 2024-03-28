#!/usr/bin/python3
# this script takes in states and lists list cities

import sys
import MySQLdb

def list_cities_by_state(username, password, db_name, state_name):
    try:
        # Connect to MySQL server
        db = MySQLdb.connect(host="localhost",
                             port=3306,
                             user=username,
                             passwd=password,
                             db=db_name)

        # Create a cursor object using cursor() method
        cursor = db.cursor()

        # Prepare SQL query
        query = "SELECT cities.id, cities.name, states.name FROM cities \
                 INNER JOIN states ON cities.state_id = states.id \
                 WHERE states.name = %s ORDER BY cities.id ASC"

        # Execute the SQL command with sanitized inputs
        cursor.execute(query, (state_name,))

        # Fetch all the rows in a list of tuples
        results = cursor.fetchall()

        # Display results
        for row in results:
            print(row)

    except MySQLdb.Error as e:
        print("MySQL Error:", e)
    finally:
        # Close the database connection
        if db:
            db.close()

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database_name> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    list_cities_by_state(username, password, db_name, state_name)