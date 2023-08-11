#! /usr/bin/python3


#Write a Python program to test whether a passed letter is a vowel or not.
lower_vowels = ['a','e','i','o','u']
x = input("Please Enter a Char: ")
if x.lower() in lower_vowels:
    print (x," is a Vowel Char")
else:
    print (x, "is not a Vowel Char")