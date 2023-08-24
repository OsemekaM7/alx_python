import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Take arguments from the command line
    username, password, dbname = sys.argv[1], sys.argv[2], sys.argv[3]
    
    # Create an engine
    engine = create_engine(f'mysql://{username}:{password}@localhost:3306/{dbname}')
    
    # Bind the engine to the base
    Base.metadata.bind = engine
    
    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Query State objects containing the letter 'a' and order by id
    states_with_a = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()
    
    # Display the results
    for state in states_with_a:
        print(f"{state.id}: {state.name}")
    
    # Close the session
    session.close()
