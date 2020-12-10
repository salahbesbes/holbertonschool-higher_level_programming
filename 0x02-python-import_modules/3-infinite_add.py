#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    args = sys.argv
    length = len(args)

    summ = 0

    for i in range(1, length):
        summ += int(args[i])
    print("{}".format(summ))
