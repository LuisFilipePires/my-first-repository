#!/usr/bin/python3
import sys
import requests

url = "https://api.github.com/user"
user = sys.argv[1]
token = sys.argv[2]

r = requests.get(url, auth=(user, token))

try:
    print(r.json().get("id"))
except:
    print(None)