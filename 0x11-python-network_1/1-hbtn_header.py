#!/usr/bin/python3
""" urllib module """
from urllib.request import Request, urlopen
import sys

if __name__ == "__main__":
    """ displays the value of the X-Request-Id """
    url = sys.argv[1]
    req = Request(url)

    with urlopen(req) as response:
        value = response.getheader('X-Request-Id')
        print(value)
