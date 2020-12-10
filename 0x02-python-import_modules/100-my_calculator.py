#!/usr/bin/python3


if __name__ == "__main__":
    from calculator_1 import add, div, sub, mul
    import sys

    def checkForOperator(op):
        ar = ["+", "-", "/", "*"]
        operation = [add, sub, div, mul]
        if (op in ar):
            for i in range(0, len(ar)):
                if (op == ar[i]):
                    return operation[i]

        else:
            return 0

    args = sys.argv
    length = len(args)

    if (length - 1 != 3):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        operation = checkForOperator(args[2])
        if (operation == 0):
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        else:
            ar1 = int(args[1])
            ar2 = int(args[3])
            print("{} {} {} = {}".format(
                ar1, args[2], ar2, operation(ar1, ar2)))
