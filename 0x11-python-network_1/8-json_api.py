#!/usr/bin/python3
"""sends a POST request to http://0.0.0.0:5000/search_user
with a letter as a parameter"""

import requests
import sys

if __name__ == '__main__':
    try:
        param = {"q": sys.argv[1]}
    except IndexError:
        param = {"q": ""}
    req = requests.post('http://0.0.0.0:5000/search_user', data=param)
    try:
        print(f"[{req.json()['id']}] {req.json()['name']}")
    except requests.exceptions.JSONDecodeError:
        print("Not a valid JSON")
    except KeyError:
        print("No result")
