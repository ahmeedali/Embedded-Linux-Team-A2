#! /usr/bin/python3

#Write a Python program to write a “list” to a file.

list_of_colors = ['red','yellow','green','blue']

with open("test.txt",'w+') as file:
    file.write(" ".join(list_of_colors)) 