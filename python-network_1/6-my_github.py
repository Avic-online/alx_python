#!/usr/bin/python3
# github info collection and display

import requests
import sys

# function to get github user id
def get_github_user_id(username, access_token):
    # url assignment
    url = 'https://api.github.com/user'

    # Set up the Basic Authentication with username and access token
    auth = (username, access_token)

    # Send GET request to fetch user information
    response = requests.get(url, auth=auth)

    # Check if request was successful (status code 200)
    if response.status_code == 200:
        user_info = response.json()
        print("Your GitHub user ID is:", user_info['id'])
    else:
        print("Failed to fetch user information. Status code:", response.status_code)

if __name__ == "__main__":
    # Get username and personal access token from command line arguments
    username = sys.argv[1]
    access_token = sys.argv[2]

    # Call function with provided credentials
    get_github_user_id(username, access_token)