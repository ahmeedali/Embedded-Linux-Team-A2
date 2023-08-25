#Lab(2)
 def my_func(**Kids):
      print(f"The parameters passed are: {Kids.items()}") #access the parameters as you access a dict

my_func(name1="Menna",name2="Mona",name3="Wael",name4="KOKO") #will print list of tuples ..each tuple contains Key and Value of each parameter
    
def my_func(*Kids):
      print(f"The parameters passed are: {Kids}")
      print(f"The parameters passed are: {Kids[2]}")    #access the parameters as you access a list

my_func("Menna","Mona","Wael")  #will print a list of the arguments passed to a function 
####################################################################################
# lab(2): multiplying a string:
a="01 "
print(a*5) 
####################################################################################
# lab(2): the order doesn't matter when passing an argument to a functon:
def my_func(child3,child2,child1):
     print("the order of the kids is :",child1,child2,child3)

my_func(child1="Tomas",child2="YoKo",child3="Fredy") 
####################################################################################
#lab(2): finding the largest number in a list:
def find_largest(*args):
   ls=list
   for i in args:
        ls.append(i)
   ls.sort()   #to make the largest element the last element
   print("The max element is:",ls[-1])

find_largest(55,40,30,99,70,85) 
####################################################################################
#Lab(): Says a sentence that you write:
from gtts import gTTS
import vlc
myobj = gTTS(text='Good Morning ShoSho,', lang='en', slow=False)
# Saving the converted audio in a mp3 file named
myobj.save("welcome.mp4")
# Playing the converted file
p = vlc.MediaPlayer("./welcome.mp4")
x = p.get_length()
p.play()
while  True:
      pass
######################################################################################
