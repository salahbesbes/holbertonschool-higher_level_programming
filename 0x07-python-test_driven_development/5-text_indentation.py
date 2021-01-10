#!/usr/bin/python3
""" no module """


def text_indentation(text):
    
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    prev = 0
    for i, ch in enumerate(text):
        if ch in ['?', ':', '.']:
            print(text[prev:i])
            print()
            if text[i + 1] == " ":
                prev = i + 2
            else:
                prev = i + 1
    print(text[prev:], end="")
