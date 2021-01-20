#!/usr/bin/python3
""" module """
import json
import sys
dump = __import__("5-save_to_json_file").save_to_json_file
load = __import__("6-load_from_json_file").load_from_json_file


def main(argv):
    """ create a json file from agumets given to the program """
    try:
        old = load("add_item.json")
        new = old + sys.argv[1:]
        dump(new, "add_item.json")
    except Exception as e:
        with open("add_item.json", mode="w") as file:
            file.write(json.dumps([]))


if __name__ == "__main__":
    main(sys.argv)
