#!/usr/bin/python3
# model states fetcher

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def print_first_state(username, password, db_name):
    # Create engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(username, password, db_name))

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Query the first State object
        first_state = session.query(State).order_by(State.id).first()

        if first_state:
            print("{}: {}".format(first_state.id, first_state.name))
        else:
            print("Nothing")
    except Exception as e:
        print("Error:", e)
    finally:
        # Close the session
        session.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database_name>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    print_first_state(username, password, db_name)