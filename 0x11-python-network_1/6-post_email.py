#!/usr/bin/python3
"""sends a POST request to a given URL with the email as a
parameter and displays the body of the response"""

import requests
import sys

if __name__ == '__main__':
    param = {'email': sys.argv[2]}
    req = requests.post(sys.argv[1], data=param)
    print(f"{req.text}")
