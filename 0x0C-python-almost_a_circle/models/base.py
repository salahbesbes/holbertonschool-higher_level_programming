#!/usr/bin/python3
""" module """
import json
import csv


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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ write int scv file
        :param list_objs: list
        """
        className = cls.__name__ + ".csv"
        with open(className, 'w', encoding="utf8") as csvfile:
            if list_objs is None:
                list_objs = []
            if cls.__name__ == "Rectangle":
                attrs = ["id", "width", "height", "x", "y"]
            elif cls.__name__ == "Square":
                attrs = ["id", "size", "x", "y"]
            writer = csv.DictWriter(csvfile, fieldnames=attrs)
            for inst in list_objs:
                writer.writerow(inst.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
            :param: class
        :return: list of instance
        """
        className = cls.__name__ + ".csv"
        result = []
        try:
            with open(className, mode="r", encoding="utf8") as csvfile:
                if cls.__name__ == "Rectangle":
                    attrs = ["id", "width", "height", "x", "y"]
                elif cls.__name__ == "Square":
                    attrs = ["id", "size", "x", "y"]
                reader = csv.DictReader(csvfile, fieldnames=attrs)
                for row in reader:
                    for key, val in row.items():
                        row[key] = int(val)
                    result.append(cls.create(**row))
                return result
        except FileNotFoundError:
            return result

    @staticmethod
    def draw(list_rectangles, list_squares):
        pass
