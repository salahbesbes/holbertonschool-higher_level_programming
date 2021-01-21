#!/usr/bin/python3
""" no module """


def append_after(filename="", search_string="", new_string=""):
    """ insert text """
    count = 0
    line = None  # initial count of characters
    prev = ""
    with open(filename, 'r+') as f:  # open file for reading an writing
        for line in f:
            prev += line
            if search_string in line:
                prev += new_string
        f.seek(0)
        f.write(prev)
