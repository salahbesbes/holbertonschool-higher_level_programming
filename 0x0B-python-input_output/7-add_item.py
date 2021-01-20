#!/usr/bin/python3
""" module """
import json
import sys
dump = __import__("5-save_to_json_file").save_to_json_file
load = __import__("6-load_from_json_file").load_from_json_file


def main(argv):
    """ create a json file from agumets given to the program """
    try:
        new = load("add_item.json")
    except:
        with open("add_item.json", mode="a") as file:
            new = []
    for el in sys.argv[1:]:
        new.append(el)
    dump(new, "add_item.json")


if __name__ == "__main__":
    main(sys.argv)
