#!/usr/bin/python3
"""
takes in a URL and an email address,
sends a POST request to the passed URL with the email as a parameter,
and finally displays the body of the response.
"""
import requests
import sys


def main():
    url1 = sys.argv[1]
    email = sys.argv[2]

    payload = {'email': email}
    response = requests.post(url1, data=payload)

    print(response.text)


if __name__ == "__main__":
    main()
