#!/usr/bin/python3
"""imports the request package"""
import requests

r = requests.get('https://alu-intranet.hbtn.io/status')
print("Body response:")

print("\t- type: ", (type(r.text)))
print("\t- content: ", r.text)
