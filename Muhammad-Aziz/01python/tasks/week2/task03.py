#! /usr/bin/python3

#Write a code to Get your public IP
import requests

x = requests.get('https://api.ipify.org/?format=json')
print(x.json()['ip'])