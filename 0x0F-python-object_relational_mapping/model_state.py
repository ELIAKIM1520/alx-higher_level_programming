#!/usr/bin/python3
"""
sqlalchemy to create a class that maps to a table
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Column, Integer

Base = declarative_base()

class State(Base):
    """Defines the class to map with the table states in the Database"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

