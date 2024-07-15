#!/usr/bin/python3
"""uses the GitHub API to display a given users id"""

import requests as r
import sys

if __name__ == '__main__':
    url = 'https://github.com/samuelodumu'
    username = sys.argv[1]
    password = sys.argv[2]

    res = r.get(url, auth=r.auth.HTTPBasicAuth(username, password))
    print(res.headers['X-GitHub-Request-Id'])
