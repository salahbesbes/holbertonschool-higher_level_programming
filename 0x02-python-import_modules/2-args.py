#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    args = sys.argv
    print(length)
    if (len(args) == 1):
        print("{} arguments.".format(length - 1))
    elif (len(args) == 2):
        print("{} argument:".format(length - 1))
    else:
        print("{} arguments:".format(length - 1))

    for i in range(1, len(args)):
        print("{}: {}".format(i, args[i]))
