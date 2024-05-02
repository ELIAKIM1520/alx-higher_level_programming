#!/usr/bin/python3
""" similar to model_state that contains a class definition of a City"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey

Base = declarative_base()


class City(Base):
    """ Maps to the database table city and also a class object definition"""
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
