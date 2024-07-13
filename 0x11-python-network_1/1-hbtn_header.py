#!/usr/bin/python3
"""sends a request to a given URL and displays the value of
the `X-Request-Id` variable"""

from urllib.request import Request, urlopen
import sys

if __name__ == '__main__':
    req = Request(sys.argv[1])
    with urlopen(req) as response:
        print(response.info()['X-Request-Id'])
