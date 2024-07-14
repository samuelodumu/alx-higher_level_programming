#!/usr/bin/python3
"""takes in a URL, sends a request to the URL and displays
the body of the response (decoded in utf-8)"""

import requests

if __name__ == '__main__':
    req = requests.get('https://alx-intranet.hbtn.io/status')
    print(f"Body response:\n\t- type: {type(req.text)}"
          f"\n\t- content: {req.text}")
