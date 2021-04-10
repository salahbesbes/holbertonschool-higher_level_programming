#!/usr/bin/python3
from urllib.request import urlopen
url = 'https://intranet.hbtn.io/status'

with urlopen(url) as response:
    decoder: str = response.getheader('Content-Type')
    decoder = decoder.split(sep="=")[1]
    content = response.read()
    print("Body response:\n\
            - type: <class 'bytes'>\n\
            - content: {}\n\
            - utf8 content: {}\
          ".format(content, content))
