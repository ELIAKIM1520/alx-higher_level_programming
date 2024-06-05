#!/usr/bin/python3
""" make cities represent a relationship with the class City
  => if the State object is deleted, all linked City objects must be deleted
  => The reference from a City object to his state should be named state
"""
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from relationship_city import Base, City


class State(Base):
    """ Maps with the states table in the database"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref='state', cascade='all, delete')
