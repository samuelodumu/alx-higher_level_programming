#!/usr/bin/python3
"""takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter, and
displays the body of the response (decoded in utf-8)"""

from urllib.request import Request, urlopen
from urllib.parse import urlencode
import sys

if __name__ == '__main__':
    value = {'email': sys.argv[2]}
    email = urlencode(value)
    email = email.encode()
    req = Request(sys.argv[1], email)
    with urlopen(req) as response:
        data = response.read()
        result = data.decode('utf')
        print(result)
