#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status using urllib"""
import urllib.request as url

req = url.Request('https://alx-intranet.hbtn.io/status')
with url.urlopen(req) as file:
    page_content = file.read()

print(page_content)
