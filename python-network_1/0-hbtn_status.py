#!/usr/bin/python3
# This program will import a request
# it is using a specific uniform resource locator and header

import urllib.request
import requests

# url = https://alu-intranet.hbtn.io/status

# # url that we are to link to

# response = requests.get(url)

# # this is the method, get, used

# print(response.status_code)

# # our print statement

# print(response.text)
if __name__ == "__main__":
    request = urllib.request.Request('https://alu-intranet.hbtn.io/status')
    with urllib.request.urlopen(request) as response:
        body = response.res()
        print('Body response:')
        print('\t- type: {}'.format(type(body)))
        print('\t- content: {}'.format(body))
        print('\t- utf8 content: {}'.format(body.decode('utf-8')))