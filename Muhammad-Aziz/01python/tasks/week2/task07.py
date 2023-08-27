#! /usr/bin/python3

#Write a Python program to count the number of words in a text file.

file = open('/home/muhammadz99/embedded_linux/test.txt','r+')
wordsInLine = []
count = 0
for x in file.readlines():
    wordsInLine = x.split()
    count += len(wordsInLine) 

print(count)
