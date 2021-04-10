#!/usr/bin/python3
""" urllib module """
from urllib.request import Request, urlopen
from urllib.parse import urlencode
import sys

if __name__ == "__main__":
    """     sends a POST request to the passed URL with the email as a parameter,
            and displays the body of the response (decoded in utf-8)
    """

    url = sys.argv[1]
    email = sys.argv[2]
    values = {'email': email}

    data = urlencode(values)
    data = data.encode('ascii')

    req = Request(url, data)
    with urlopen(req) as response:
        the_page = response.read()
        print(the_page.decode('ascii'))
