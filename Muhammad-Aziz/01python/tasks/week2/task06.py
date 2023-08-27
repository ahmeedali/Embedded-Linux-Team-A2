#! /usr/bin/python3

#Write a Python program to count the number of lines in a text file.

file = open('/home/muhammadz99/embedded_linux/test.txt','r+')
lines = file.readlines()
print(len(lines))
