#!/usr/bin/python3

ls = [1,4,5,88,4,13,4,1,13]

n = 0

x = int(input("Please enter number: "))

for i in ls:
    if i == x:
        n += 1

print(n)

        