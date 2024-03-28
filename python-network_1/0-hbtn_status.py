#!/usr/bin/python3
# python code to show hbtn status

import requests

# function to fetuc status
def fetch_status():
    # url to be fetched
    url = 'https://alu-intranet.hbtn.io/status'
    response = requests.get(url)
    
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))

if __name__ == "__main__":
    fetch_status()
