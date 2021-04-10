#!/usr/bin/python3
""" requests module """
from requests import post
import sys

if __name__ == "__main__":
    """     sends a POST request to the passed URL with the email as a parameter,
            and displays the body of the response
    """

    url = sys.argv[1]
    email = sys.argv[2]
    values = {'email': email}

    res = post(url, values)
    print(res.text)
