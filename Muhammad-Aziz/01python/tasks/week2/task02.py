#! /usr/bin/python3

#Write a code to suggest automatically activates for you
import requests

x = requests.get('https://www.boredapi.com/api/activity')
print(x.json()['activity'])