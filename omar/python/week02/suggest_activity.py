#!/usr/bin/python3

from requests import request

# Function that send request to suggesting activity site and print the activity
def suggest_activity():
    response = request("get", "https://www.boredapi.com/api/activity")
    suggested_activity = response.json()["activity"]
    print(suggested_activity)

if __name__ == "__main__":
    suggest_activity()
