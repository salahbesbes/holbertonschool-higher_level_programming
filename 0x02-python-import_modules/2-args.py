#!/usr/bin/python3

import sys

args = sys.argv
length = len(args)
if (len(args) == 1):
    print('{} arguments.'.format(length - 1))
else:
    print('{} arguments:'.format(length - 1))

for i in range(1, len(args)):
    print("{}: {}".format(i, args[i]))
