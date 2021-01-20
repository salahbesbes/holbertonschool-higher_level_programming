#!/usr/bin/python3
""" no module """


def append_after(filename="", search_string="", new_string=""):
    """ insert text """
    count = 0
    line = None  # initial count of characters
    prev = ""
    with open(filename, 'r+') as f:  # open file for reading an writing
        while line != "":
            line = f.readline()
            prev += line
            if search_string in line:
                # place cursor at the correct character location
                count = f.tell()
                remainder = f.read()  # store all character afterwards
                f.seek(0)
            # insert text and rewrite the remainder
                f.write(prev + new_string + remainder)
                f.seek(count)
