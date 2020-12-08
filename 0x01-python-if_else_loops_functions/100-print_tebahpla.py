#!/usr/bin/python3
for i in range(ord('z'), ord('a') - 1, -1):
    if i % 2 != 0:
        i -= 32
    print("{}".format(chr(i)), end="")
