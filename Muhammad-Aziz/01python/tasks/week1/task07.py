#! /usr/bin/python3

#Find the largest item from a given list using loop

list1 = [1,3,5,8,2,4,5,7,8,12,11,52,17,77,53,12]
y = list1[0]
for x in list1:
    if x > y:
        y = x
print(y)

