#!/usr/bin/python3
""" module """
import json


def load_from_json_file(filename):
    """ create obj from a json file """
    with open(filename, encoding="utf-8") as file:
        return json.loads(file.read())
