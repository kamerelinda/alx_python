#!/usr/bin/python3
"""
Fetches a URL and prints the X-Request-Id header value.

"""

import requests
import sys

r = sys.argv[1]
"""sends a request to the url"""
response = requests.get(r)
"""prints the id id variable in the header"""
print(response.headers['X-Request-Id'])
