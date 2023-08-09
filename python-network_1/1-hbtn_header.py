#!/usr/bin/python3
"""This script uses request and sys"""
import requests
import sys

r = sys.argv[1]
response = requests.get(r)
print(response.headers['X-Request-Id'])
