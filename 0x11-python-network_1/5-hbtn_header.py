#!/usr/bin/python3
""" requests module """
from requests import get
import sys

if __name__ == "__main__":
    """ displays the value of the X-Request-Id """
    url = sys.argv[1]

    res = get(url)
    print(res.headers.get('X-Request-Id'))
