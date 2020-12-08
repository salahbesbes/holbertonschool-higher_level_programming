#!/usr/bin/python3
for line in range(0, 10):
    for nb in range(line + 1, 10):
        if (line * 10 + nb == 89):
            print("{:02d}".format(line * 10 + nb))
        else:
            print("{:02d}".format(line * 10 + nb), end=", ")
