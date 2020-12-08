#!/usr/bin/python3
def fizzbuzz():
    for nb in range(1, 101):
        if (nb % 15 == 0):
            print("{}". format("FizzBuzz"), end=" ")
        elif (nb % 3 == 0):
            print("{}".format("Fizz"), end=" ")
        elif (nb % 5 == 0):
            print("{}".format("Buzz"), end=" ")
        else:
            print("{}".format(nb), end=" ")
