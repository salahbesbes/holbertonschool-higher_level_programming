#!/usr/bin/python3
from urllib.request import Request, urlopen
""" urllib module """

if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'
    req = Request(url)

    with urlopen(req) as response:
        content = response.read()

        print("Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: {}"
              .format(content.__class__,
                      content,
                      content.decode('ascii')
                      ))
