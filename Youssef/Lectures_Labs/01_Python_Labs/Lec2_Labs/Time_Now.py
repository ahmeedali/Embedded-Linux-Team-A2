""" 
   Autor      :     Youssef Adel Youssef
Description   :     Print Current Date and Time.
"""

import datetime

Now = datetime.datetime.now()
print("Current Date and Time : ")
print(str(Now)[0:-7])