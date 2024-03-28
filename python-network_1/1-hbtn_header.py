#!/usr/bin/python3
# hbtn header script

import requests
import sys

# function to fetch request id
def fetch_request_id(url):
    # function states
    response = requests.get(url)
    request_id = response.headers.get('X-Request-Id')
    print("{}".format(request_id))

if __name__ == "__main__":
    url = sys.argv[1]
    fetch_request_id(url)