#!/usr/bin/python3
""" no module """


def write_file(filename="", text=""):
    """ write text to a file """
    with open(filename, mode="w", encoding="utf-8") as file:
        return file.write(text)
