#!/usr/bin/python3

mydata = {'Full Name' : 'Omar Hosny Kamal',
            'Birth Date' : '6/6/1997',
            'Faculty': 'EME',
            'Email' : 'omarhosny58@gmail.com',
            'Address' : 'Alexandria'}

for key,value in mydata.items():
    print(key +': ' + value)