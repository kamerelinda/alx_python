#!/usr/bin/python3
"""This script uses request and sys"""
import requests
import sys
"""Takes in a URL, sends a request to the URL and displays 
the value of the variable X-Request-Id in the response header"""
r = sys.argv[1]
response = requests.get(r)
print(response.headers['X-Request-Id'])
