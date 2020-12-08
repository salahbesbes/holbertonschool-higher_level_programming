def print_last_digit(number):
    nb = number
    last_digit = nb % 10
    if (number < 0):
        nb = -nb
        last_digit = nb % 10

    print("{:d}".format(last_digit), end="")
    return(last_digit)
