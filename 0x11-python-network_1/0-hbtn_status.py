#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status using urllib"""

if __name__ == '__main__':
    import urllib.request as url
    req = url.Request('https://alx-intranet.hbtn.io/status')
    with url.urlopen(req) as response:
        data = response.read()
        utf_data = data.decode()
        content_type = type(data)
        print(f'Body response:\n\t- type: {content_type}\n\t- content: {data}'
              f'\n\t- utf8 content: {utf_data}')
