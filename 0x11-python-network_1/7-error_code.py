#!/usr/bin/python3
""" requests module """
from requests import get
import sys

if __name__ == "__main__":
    """     sends a request to the URL and displays the body
            of the response. and handle ERROR
    """

    url = sys.argv[1]
    res = get(url)
    if res.status_code > 400:
        print("Error code: {}".format(res.status_code))
    else:
        print(res.text)
