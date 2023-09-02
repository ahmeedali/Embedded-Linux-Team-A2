""" 
   Autor      :   Youssef Adel Youssef
Description   :   Write a code to print datetime informations
"""

import datetime

DateTime = datetime.datetime.now()
print(DateTime.strftime("%Y %B %d - %H:%M:%S - %A"))