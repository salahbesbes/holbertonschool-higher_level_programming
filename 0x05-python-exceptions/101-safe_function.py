#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(args[0], args[1])
    except IndexError as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return None
    except ZeroDivisionError as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return None
    return result
