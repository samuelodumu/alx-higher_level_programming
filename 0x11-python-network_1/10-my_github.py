#!/usr/bin/python3
"""uses the GitHub API to display a given users id"""

import requests
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    url = f'https://api.github.com/user'
    header = {"Authorization": f"Bearer {password}"}

    res = requests.get(url, headers=header)
    json_res = res.json()

    if res.status_code >= 400:
        print('None')
    else:
        print(json_res.get('id'))
