#!/usr/bin/python3
""" The Script deletes all State objects with the name containing `a` from db"""
import sys
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """Define the State class"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

if __name__ == '__main__':
    try:
        engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                               .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                               pool_pre_ping=True)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()

        # Retrieve and delete State objects with names containing 'a'
        states_with_a = session.query(State).filter(State.name.like('%a%')).all()
        for state in states_with_a:
            session.delete(state)
        
        session.commit()
        print("Deleted State objects with names containing 'a'")
    
    except Exception as e:
        print("An error occurred:", e)

    finally:
        if session:
            session.close()

