"""
This program will import a request
it is using a specific uniform resource locator and header
"""

import requests

url = https://alu-intranet.hbtn.io/status

response = requests.get(url)

print(response.status_code)

print(response.text)