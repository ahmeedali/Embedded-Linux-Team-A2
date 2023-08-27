#!/usr/bin/python3

import requests

url = requests.get ("https://api.ipify.org/?format=json")
ip  = url.json()["ip"]
url2= requests.get(f"https://api.iplocation.net/?ip={ip}")
print(url2.json())