#!/usr/bin/python3
""" requests module """
from requests import post, get
from requests.models import HTTPBasicAuth
import sys


def get_date(element):
    return element.get('commit').get('author').get('date')


if __name__ == "__main__":
    """     takes your GitHub credentials (username and password)
            and uses the GitHub API to display your id
    """

    repo_name = sys.argv[1]
    username = sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(
        username, repo_name)

    res = get(url)

    try:
        result = res.json()
        # result = sorted(result, key=get_date)

        for obj in result[:10]:
            print("{}: {}".format(
                obj.get('sha'),
                obj.get('commit').get('author').get('name')
            ))
    except Exception:
        pass
