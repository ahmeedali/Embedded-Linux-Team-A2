#!/usr/bin/python3


print ("Please enter bits mode '0' for input mode '1' for output mode ")
bits=[]
for bit in range (8): 
    while True:
       m =(input (f"Please enter bit {bit} mode : "))     
     
       if m == "0"  :
                bits.append('0')
                break
       elif m.lower() == "1" :
                bits.append('1')
                break
       else:
                print("invalid input")

bits.reverse()
b = "".join(bits)
            
            
Init = open("GPIO.c","w")

GPIO = f'#include "avr/io.h"\n\
        void Init_PORTA_GPIO(void)\n\
        {{\n\
            DDRA = 0b{b};\n\
        }}'
Init.write(GPIO)



