#!/usr/bin/python3
""" requests module """
from requests import post, get
from requests.models import HTTPBasicAuth
import sys
if __name__ == "__main__":
    """     takes your GitHub credentials (username and password)
            and uses the GitHub API to display your id
    """

    username = sys.argv[1]
    token = sys.argv[2]

    url = 'https://api.github.com/user'
    # url = 'https://api.github.com/user/{}'.format(username)

    res = get(url, auth=('username', token))
    try:
        print(res.json().get('id'))
    except Exception:
        print('None')
