#!/usr/bin/python3

import calendar

print("Welcome to the calendar program")

y = int(input("Enter the year: "))
m = int(input("Enter the month: "))

print("\n" + calendar.month(y,m,3,1))