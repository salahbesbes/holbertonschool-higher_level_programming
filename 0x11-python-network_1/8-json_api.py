#!/usr/bin/python3
""" requests module """
from requests import post
import sys

if __name__ == "__main__":
    """     handle a search request
    """
    url = 'http://0.0.0.0:5000/search_user'
    url = 'http://848dc111ec81.b380b380.hbtn-cod.io:5000/search_user'
    try:
        letter = sys.argv[1]
    except Exception:
        letter = ''
    res = post(url, data={'q': letter})

    try:
        result = res.json()
        if result:
            print("[{}] {}".format(result.get('id'), result.get('name')))
        else:
            print('No result')
    except Exception:
        print('Not a valid JSON')
