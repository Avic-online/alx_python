#!/usr/bin/python3
"""This program will import a request it is using a specific url"""
# import requests

# url = 'https://alu-intranet.hbtn.io/status'

# response = requests.get(url)

# if response.status_code == 200:
#     data = response.json()
#     print("- Raw Body response:")
#     print("\t- type:", type(data))
#     print("\t- content:", data)
# else:
#     print(f"Failed to fetch data. Status code: {response.status_code}")


import requests

if __name__ == "__main__":
    request = requests.Request('https://intranet.hbtn.io/status')
    with requests.urlopen(request) as response:
        body = response.read()
        print('body response:')
        print('\t- type: {}'.format(type(body)))
        print("\t- content: {}".format(type(body)))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))