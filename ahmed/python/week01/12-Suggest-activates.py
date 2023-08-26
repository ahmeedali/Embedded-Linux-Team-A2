#!/usr/bin/python3

import requests

print ("Choose one or more activity of 10 activities")
for i in range(10):
    url = requests.get ("https://www.boredapi.com/api/activity")
    print("- " + url.json()['activity'])
print ("\n Enjoy ^_^ \n")    