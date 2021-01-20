#!/usr/bin/python3
""" no module """


def append_write(filename="", text=""):
    """ append to file """
    with open(filename, mode="a", encoding="utf-8") as file:
        return file.write(text)
