def uppercase(str):
    for char in str:
        if (ord(char) in range(ord('a'), ord('z') + 1)):
            char = chr(ord(char) - 32)
        print("{}".format(char), end="")
    print()
