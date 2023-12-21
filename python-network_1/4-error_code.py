"""
This program imports requests and sys
it is melt to display error codes
"""

import requests
import sys

def fetch_and_display(url):
    try:
        response = requests.get(url)
        print(response.text)
        if response.status_code >= 400:
            print("Error Code: {}".format(requests.status_codes))

    except requests.RequestException as e:
        print("Error: {}".format(e))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <URL>")
    else:
        url = sys.argv[1]
        

        fetch_and_display(url)