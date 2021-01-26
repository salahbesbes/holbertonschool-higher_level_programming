#!/usr/bin/python3
""" no module """

def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in range(len(text)):
        if not (text[i] == ' ' and text[i - 1] in [':', '.', '?']):
            print(text[i], end="")
        if text[i] in [':', '.', '?']:
            print()
            print()
