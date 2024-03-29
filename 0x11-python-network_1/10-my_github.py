#!/usr/bin/python3
""" script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
import sys
import requests
from requests.auth import HTTPBasicAuth
from sys import argv

if __name__ == '__main__':
    url = 'https://api.github.com/users/{}'.format(argv[1])
    response = requests.get(url,
                            auth=HTTPBasicAuth(argv[1], argv[2]))
    print(response.json().get('id'))
