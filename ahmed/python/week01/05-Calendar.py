#!/usr/bin/python3
import calendar
choise = input ('year or month: ')

if choise.strip().lower() == 'month' :
    m = int (input ('please enter the month: '))
    y = int (input ("please enter the year: "))
    print (calendar.month(y,m))
elif choise.strip().lower() == 'year':
    y = int (input ("please enter the year: "))
    print (calendar.calendar(y))
else :
    print ("invalid input")