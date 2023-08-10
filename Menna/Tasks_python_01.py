#Task(1)
#ls=[1,2,3,3,55,5,5,5,9,9,9,9,10]
#v= int(input("Please enter the number you want to count: "))
#if v in ls :
#    print(f"The count of {v} is {ls.count(v)}")
#else :
#   print(f"{v} is not in the list ")  
############################################################################
#vowles="a e o u i A E O U I" 
#char = input("the char you want to check: ")
#if char in vowles:
#    print(f"The character '{char}' is a vowel!")
#else:
#    print(f"The character '{char}' is a consonant!")  
#############################################################################
#import os
#print("the list of the ENV. variables :")
#print(os.environ) 
#print(os.environ['HOME']) #to access definit variable
############################################################################ 
#task(2)
#import math
#v=float(input("Please enter the radius: "))
#Area=(math.pi)*v**2
#print("The Area is:%f"%Area)
#print(f"The Area is:{Area}")  #when you want to print more than 1 variable inside a string
#print("The Area is: "+ str(Area))
#print("The Area is: ",Area)   #only with print func
############################################################################
# task(3) 
#year = int(input("please enter the year:"))
#month = int(input("please enter the month:"))
#print(calendar.month(year,month))
###########################################################################
#from pytube import YouTube
#URL=input("please enter the video url :")
#YouTube('{URL}').streams.filter(progressive=True,file_extension='mp4').first().download()
###########################################################################
