#!/usr/bin/python3
"""imports the request package"""
import requests


def main():

    r = requests.get('https://alu-intranet.hbtn.io/status')
    print("Body response:")

    print("\t- type:", (type(r.text)))
    print("\t- content:", r.text)


if __name__ == "__main__":
    main()
