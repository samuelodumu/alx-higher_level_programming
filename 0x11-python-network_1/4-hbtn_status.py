#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status using requests"""

import requests

if __name__ == '__main__':
    req = requests.get('https://alx-intranet.hbtn.io/status')
    print(f"Body response:\n\t- type: {type(req.text)}"
          f"\n\t- content: {req.text}")
