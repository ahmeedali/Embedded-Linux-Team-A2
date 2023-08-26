#Lab(04): Applications on using OS library + Files Operations:
#Task:counting no. of words and lines of a text file
import os 
print(os.curdir)
print(os.getcwd())
if not os.path.exists("Test") :
  os.makedirs("Test")
with open("Test/"+"Menna"+".txt","w") as f:   #with ..as closes the file automatically as it ends
    f.writelines("Hello This is Menna.") 
file=open("Test/"+"Menna"+".txt","r")  # note r
wordCount=file.read().split().__len__()        #Counting no of words
print(wordCount)

#Note: you cant read the file twice ...only one time then perform your operations

sentences=file.readlines().__len__()           #Counting no of lines
print(sentences)
file.close()  

#Another method:
count=0
#sentences=file.readlines()             #list of the sentences presented
for line in sentences:
   wordsinline=line.split()
   print(wordsinline)
   count=count+wordsinline.__len__()  #Quick task 1 counting words in file
file.close()   
print(count)  
 """

 
#os.remove("the file name you want to remove.type")
#os.rmdir("the folder name to be removed")
 
