""" 
   Autor      :     Youssef Adel Youssef
Description   :     Choose Number of the folder you need to open.
"""

import os

Favourite_Floader = [
    "/home/youssef/Documents",
    "/home/youssef/Pictures"
]

Val = int(input("Please Select Your Dir (index start with 0) : "))

os.popen(r"nautilus {}".format(Favourite_Floader[Val]))