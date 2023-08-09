#!/usr/bin/python3
import requests
import sys

"""takes in url as the first argument """
r = sys.argv[1]
"""sends a request to the url"""
response = requests.get(r)
"""prints the id id variable in the header"""
print(response.headers['X-Request-Id'])
