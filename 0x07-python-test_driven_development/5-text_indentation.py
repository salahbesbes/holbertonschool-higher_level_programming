#!/usr/bin/python3
""" no module """


def text_indentation(text):
    
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    line = ""
    for ch in text:
        line += ch
        if ch in ['.', ':', '?']:
            if line[0] == " ":
                print(line[1:])
            else:
                print(line)
            line = ""
            print()
        else:
            print(ch, end="")

