#!/usr/bin/python3

from requests import request

# Function that returns public Ip
def public_ip() -> str:
    # Requesting response from public IP site
    response = request("get", "https://api.ipify.org/?format=json")
    ip = response.json()["ip"]
    return ip

if __name__ == "__main__":
    print(public_ip())

