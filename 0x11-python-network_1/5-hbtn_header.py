#!/usr/bin/python3
""" cript that takes in a URL, sends a request to the URL and displays the
value of the variable X-Request-Id in the response header
"""
import requests
from sys import argv

if __name__ == '__main__':
    re = requests.get(argv[1])
    print(re.headers.get('X-Request-Id'))
