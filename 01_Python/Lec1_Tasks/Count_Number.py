""" 
   Autor      :   Youssef Adel Youssef
Description   :   Program to count the required number on a given list.
"""

List_Numbers = [4, 2, 5, 8, 9, 4, 6, 4, 1, 7, 3, 8, 5, 3, 2, 5]
Req_Number = int(input("Input the Required Number for Searching : "))
Count = List_Numbers.count(Req_Number)
print("The Number of 4s in the List is : {}".format(Count))