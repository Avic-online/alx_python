#!/usr/bin/python3
# this script posts email

import requests
import sys

# function to send post requests
def send_post_request(url, email):
    # assignment and display
    payload = {'email': email}
    response = requests.post(url, data=payload)
    print(response.text)

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    send_post_request(url, email)
