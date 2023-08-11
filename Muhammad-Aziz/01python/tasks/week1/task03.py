#! /usr/bin/python3

#Write a python program to access environment variables.
import os
# Access all environment variables 
print(os.environ)
# Access a particular environment variable 
print(os.environ['HOME'])

print(os.environ['PATH'])
