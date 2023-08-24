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
    
    # Query the first State object ordered by id
    first_state = session.query(State).order_by(State.id).first()
    
    # Display the result
    if first_state is None:
        print("Nothing")
    else:
        print(f"{first_state.id}: {first_state.name}")
    
    # Close the session
    session.close()
