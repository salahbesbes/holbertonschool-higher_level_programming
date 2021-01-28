#!/usr/bin/python3
""" module """
import json


class Base:
    """ class base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ init class  """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ static method that transform list of dict to str format json
        :param list_dictionaries:
        :return: str
        """
        if list_dictionaries is None:
            return json.dumps([])
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs: list):
        """ create a json file from arguments given to the program
        :param list_objs: list
        """
        className = cls.__name__ + ".json"
        with open(className, mode="w") as file:
            if list_objs is None:
                list_objs = []
            newJson = [inst.to_dictionary() for inst in list_objs]
            file.write(cls.to_json_string(newJson))

    def from_json_string(json_string):
        """
            transform a string format json to a dict
        :return: list of dict
        """
        if json_string:
            return json.loads(json_string)
        else:
            return []

    @classmethod
    def create(cls, **dictionary):
        """
            create new instance based on **dict
        :param dictionary: dict
        :return: new instance
        """
        dummy = cls(55, 66)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
            open file and read all content
        :return: content of a file
        """
        className = cls.__name__ + ".json"
        arAttrs = []
        try:
            with open(className, mode="r") as file:
                content = file.read()
                listOfDicts = cls.from_json_string(content)
                for instDict in listOfDicts:
                    newInst = cls.create(**instDict)
                    arAttrs.append(newInst)
                return arAttrs
        except FileNotFoundError:
            return []
