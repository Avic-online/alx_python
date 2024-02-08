#!/usr/bin/python3
"""This program will import a request it is using a specific url"""
import requests

url = 'https://alu-intranet.hbtn.io/status'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("- Raw Body response:")
    print("\t- type:", type(data))
    print("\t- content:", data)
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")