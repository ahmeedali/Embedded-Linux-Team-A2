#!/usr/bin/python3
from pytube  import *
from tqdm    import *
from time    import *

url = input ("please enter video url: ") 

#pixel = input ("please enter reslution EX [ 720p,480p,360p,240p,144p ] : ")
#tqdm bar not accurate time but nice simlution 
for i in tqdm (YouTube(url).streams.get_highest_resolution().download()) :
    sleep(0.1)
print ("Done")