#!/usr/bin/python3
"""takes in a URL, sends a request to the URL and displays
the body of the response (decoded in utf-8)"""

from urllib.request import Request, urlopen
from urllib.error import HTTPError
import sys

if __name__ == '__main__':
    req = Request(sys.argv[1])
    try:
        response = urlopen(req)
    except HTTPError as e:
        print(f"Error code: {e.code}")
    else:
        print(response.read().decode())
