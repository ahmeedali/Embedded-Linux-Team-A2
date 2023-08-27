#! /usr/bin/python3

#Write a code to Get your public IP
import requests

ip_res = requests.get('https://api.ipify.org/?format=json')
ip = ip_res.json()['ip']
link = 'https://ipinfo.io/'+ip+'/geo'
x = requests.get(link)

print("City: " + x.json()['city'])
print("Region: " + x.json()['region'])
print("Country: " + x.json()['country'])