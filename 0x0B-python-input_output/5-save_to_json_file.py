#!/usr/bin/python3
""" modules """
import json


def save_to_json_file(my_obj, filename):
    """ writes an Object to a text file """
    with open(filename, encoding="utf-8", mode="w") as file:
        file.write(json.dumps(my_obj))
