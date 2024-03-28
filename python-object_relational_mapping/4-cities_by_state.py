#!/usr/bin/python3
# script to ist cities in a state

import sys
import MySQLdb

def list_cities(username, password, db_name):
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
        query = "SELECT * FROM cities ORDER BY id ASC"

        # Execute the SQL command
        cursor.execute(query)

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
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database_name>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    list_cities(username, password, db_name)