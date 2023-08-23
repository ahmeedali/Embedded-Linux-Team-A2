#!/usr/bin/python3

from requests import request

def location() -> str:
    # Requesting geolocation from ipinfo site
    response = request("get", "https://ipinfo.io/what-is-my-ip#block-geolocation")
    info = response.json()
    location = info["city"] + "," + info["country"]
    return location
    
if __name__ == "__main__":
    print(location())