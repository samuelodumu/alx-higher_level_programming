#!/usr/bin/python3
"""uses the GitHub API to display a given users id"""

import requests as r
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    url = f'https://api.github.com/users/{username}'

    res = r.get(url, auth=r.auth.HTTPBasicAuth(username, password))
    if res.status_code == 200:
        print(res.json()['id'])
    else:
        print(None)
