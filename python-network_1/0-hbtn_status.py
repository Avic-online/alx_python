"""
This program will import a request
it is using a specific uniform resource locator and header
"""

import requests

url = https://alu-intranet.hbtn.io/status

# url that we are to link to

response = requests.get(url)

# this is the method, get, used

print(response.status_code)

# our print statement

print(response.text)