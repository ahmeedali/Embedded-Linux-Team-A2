""" 
   Autor      :   Youssef Adel Youssef
Description   :   Print the calendar for a given month and year.
"""

import calendar
Year = int(input("Input The Year : "))
Month = int(input("Input The month : "))
print(calendar.month(Year , Month))