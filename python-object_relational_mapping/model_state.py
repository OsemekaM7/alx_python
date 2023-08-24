from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# Create a declarative base
Base = declarative_base()
# Define the State class
class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)

# Define the connection to the MySQL server
engine = create_engine('mysql://username:password@localhost:3306/dbname')

# Create a declarative base
Base = declarative_base()

# Create tables in the database
Base.metadata.create_all(engine)

# Creating a session
Session = sessionmaker(bind=engine)
session = Session()

# Close the session
session.close()
