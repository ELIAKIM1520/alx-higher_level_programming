#!/usr/bin/python3
""" make cities represent a relationship with the class City
=> if the State object is deleted, all linked City objects must be deleted
=> The reference from a City object to his state should be named state
"""
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """ Reperesent a city that maps to a table cities in db"""
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
