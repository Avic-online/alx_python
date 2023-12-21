"""
all imports are done from requests package and sys
it is a program to send email
"""

import requests
import sys

def send_post_request(url, email):
    try:
        payload = {'email': email}
        response = requests.post(url, data=payload)
        print(response.text)
    except requests.RequestException as e:
        print("Error: {}".format(e))


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script_name.py <URL> <email>")
    else:
        url = sys.argv[1]
        email = sys.argv[2]

        send_post_request(url, email)
