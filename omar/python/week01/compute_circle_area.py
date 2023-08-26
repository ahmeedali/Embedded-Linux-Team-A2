#!/usr/bin/python3

import math

r = int(input("Please enter the radius: "))

if(r > 0):
    print("Area:",(math.pi*(r**2)))
else:
    print("Invalid Input")