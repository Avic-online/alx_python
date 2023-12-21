"""
This program will import a request
it is using a specific uniform resource locator and header
"""

import requests
import sys

# url = https://www.britishairways.com/travel/home/public/en_ng/

# response = requests.get(url)

def get_x_request_id():
    try:
        response = requests.get(url)
        if response.status_code == 200:
            x_request_id = response.headers.get('X-Request-Id')
            if x_request_id:
                print("X-Request-Id: {}".format(x_request_id))
            else:
                print("X-Request-Id header not found in the response")
        else:
            print("Error: {}".format(response.status_code))
    except requests.RequestException as e:
        print("Error: {}".format(e))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <URL>")
    else:
        url = sys.argv[1]
        get_x_request_id(url)