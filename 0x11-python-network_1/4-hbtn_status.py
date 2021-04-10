#!/usr/bin/python3
""" requestes module """
from requests import get

if __name__ == "__main__":
    """ using requests module fet some data """
    url = 'https://intranet.hbtn.io/status'

    response = get(url)
    print("Body response:\n\t- type: {}\n\t- content: {}"
          .format(response.text.__class__,
                  response.text,
                  ))
