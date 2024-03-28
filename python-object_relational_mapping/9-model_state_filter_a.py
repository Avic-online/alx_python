#!/usr/bin/python3
# 9 model states filter

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def list_states_with_letter_a(username, password, db_name):
    # Create engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(username, password, db_name))

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Query State objects that contain the letter 'a'
        states_with_a = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()

        # Display results
        for state in states_with_a:
            print("{}: {}".format(state.id, state.name))
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

    list_states_with_letter_a(username, password, db_name)