#!/usr/bin/python3
"""Defines a class Student by (based on 9-student.py)
"""


class Student:
    """class student based on the 9-student.py
"""

    def __init__(self, first_name, last_name, age):
        """instantiation of our object
        Args:
        first_name (str): the first name of the student
        last_name (str): the last_name of the student
        age (int): the age of the student
"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        
    def to_json(self, attrs=None):
        """retrieves a dictionary represantation of a student instance
        if attrs is a list of strings, it represents only those attributes included in the list

        Args:
            attrs (list):attributes to represent
"""
        if (type(attrs) == list and
                all(type(item) == str for item in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
