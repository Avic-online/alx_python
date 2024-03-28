#!/usr/bin/python3
# json api fetcher

import requests
import sys

# function to search for user
def search_user(letter):
    #url assignment
    url = 'http://0.0.0.0:5000/search_user'
    payload = {'q': letter}

    # Send POST request
    response = requests.post(url, data=payload)

    try:
        # Check if response is properly JSON formatted and not empty
        json_response = response.json()
        if json_response:
            print("[{}] {}".format(json_response.get('id'), json_response.get('name')))
        else:
            print("No result")
    except ValueError:
        # Invalid JSON
        print("Not a valid JSON")

if __name__ == "__main__":
    # Get letter from command line argument
    letter = sys.argv[1] if len(sys.argv) > 1 else ""

    # Call function with the provided letter
    search_user(letter)