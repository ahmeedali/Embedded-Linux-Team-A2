#! /usr/bin/python3

#Write a Python program which accepts the radius of a circle from the user and compute the area.
import math as m
r = input ('Please Enter Radius of Circle: ')
print("Area of circle = ",m.pi*m.pow(float(r),2))