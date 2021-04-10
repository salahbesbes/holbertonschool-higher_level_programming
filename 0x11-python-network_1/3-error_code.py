#!/usr/bin/python3
""" urllib module """
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
import sys

if __name__ == "__main__":
    """     sends a request to the URL and displays the body
            of the response (decoded in utf-8). and handle ERROR
    """

    url = sys.argv[1]
    req = Request(url)
    try:

        with urlopen(req) as response:
            the_page = response.read()
            print(the_page.decode('ascii'))

    except URLError as error:
        print('Error code: {}'.format(error.code))
    except HTTPError as error:
        print('Error code: {}'.format(error.code))
