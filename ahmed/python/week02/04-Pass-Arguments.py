#!/usr/bin/python3
import sys
 
#using argv for parsing arguments from command line
n = len(sys.argv)
print("Total arguments passed:", n)
 
print("\nName of Python script:", sys.argv[0])
 
print("\nArguments list :", end = " ")
for i in range(1, n):
    print(sys.argv[i], end = " ")
# sum arguments from command line
Sum = 0
for i in range(1, n):
    Sum += int(sys.argv[i])
     
print("\n\nResult:", Sum)
     
