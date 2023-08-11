#!/usr/bin/python3
"""
This script takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
import requests
import sys


def main():
    username = sys.argv[1]
    pat_password = sys.argv[2]

    response = requests.get('https://api.github.com/user', auth=(username, pat_password))

    if response.status_code == 200:
        data = response.json()
        if data:
            print(data['id'])
    else:
        print(None)


if __name__ == "__main__":
    main()
