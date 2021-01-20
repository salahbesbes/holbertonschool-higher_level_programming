#!/usr/bin/python3
""" no module """


def read_file(filename=""):
    """ read from file """
    with open(filename, encoding="utf-8", mode="r") as file:
        print(file.read(), end="")
