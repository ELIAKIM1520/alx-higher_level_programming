#!/usr/bin/python3
"""Script that prints the first State object from the database"""
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
    username, password, database = sys.argv[1], sys.argv[2],  sys.argv[3]
    engine = create_engine(f'mysql://{username}:{password}@localhost:3306/{database}')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    f_state = session.query(State).order_by(State.id).first()
    if f_state:
        print(f'{f_state.id}: {f_state.name}')
    else:
        print('Nothing')
    session.close()

