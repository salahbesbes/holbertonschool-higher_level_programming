#!/usr/bin/python3
""" urllib module """
from urllib.request import Request, urlopen

if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'
    req = Request(url)

    with urlopen(req) as response:
        content = response.read()

        print("Body response:\n\
        - type: {}\n\
        - content: {}\n\
        - utf8 content: {}"
              .format(content.__class__, content, content.decode('ascii')))
