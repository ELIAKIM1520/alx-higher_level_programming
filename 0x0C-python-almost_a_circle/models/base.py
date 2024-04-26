#!/usr/bin/python3
""" the first class ``Base`` in the file base.py"""
import json
import csv


class Base:
    """ Represents the base model
    Represents the Base for all other classes in this project
    Attributes:
        __nb_objects (int): number of instantiated bases"""
    __nb_objects = 0

    def __init__(self, id=None):
        """instantiation of our class object
        Args:
            id (any): the id to manage in all future classes

"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the json string representation of a list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the json string representation of a list_objs to a file"""
        if list_objs is None:
            list_objs = []
        file_name = cls.__name__ + ".json"
        with open(file_name, "w") as f:
            f.write(cls.to_json_string([objs.to_dictionary() for objs in list_objs]))

    def from_json_string(json_string):
        """ returns the list of the json string representation json_string"""
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Returns a class instantiated from dict attributes
        Args:
        **dictionary (dict): key/value pairs of the attrubutes to initialize
"""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                dummy = cls(1, 1)
            else:
                dummy = cls(1)
            dummy.update(**dictionary)
            return dummy

    def load_from_file(cls):
        """ returns a list of instances"""
        filename = __class__.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                list_dicts = cls.from_json_string(file.read())
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
           return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ it writes the csv serialization of a list of objectas to a file"""
        file_name = cls.__name__ + ".csv"
        with open(file_name, 'w', newline='') as f_csv:
            if list_objs is None or list_objs == []:
                f_csv.write('[]')
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ['id', 'width', 'height', 'x', 'y']
                else:
                    fieldnames = ['id', 'size', 'x', 'y']
                writer = csv.DictWriter(f_csv, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """It returns a list of classes instantiated from a csvfile fromat
        reads from cls.__name__.csv
"""
        file_name = cls.__name__ + ".csv"
        try:
            with open(file_name, 'r', newline='') as f_csv:
                if cls.__name__ == "Rectangle":
                    fieldnames = ['id', 'width', 'height', 'x', 'y']
                else:
                    fieldnames = ['id', 'size', 'x', 'y']
                list_dicts = csv.DictReader(f_csv, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
