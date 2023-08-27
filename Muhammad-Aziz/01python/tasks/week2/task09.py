#! /usr/bin/python3

# Write python code to generate Initfunction of GPIO for AVR

import os
import math

if os.path.exists("gpio_function") == False:
    os.makedirs("gpio_function")

file_h = open('gpio_function/gpio_init.h','a+')
file_c = open('gpio_function/gpio_init.c','a+')

PORT = input("please Enter Port name: ")
BITS_str = input("Please Enter GPIO register size in bits: ")
BITS = int(BITS_str)
print("Please Enter each pin Direction")
DDR_value = 0
for i in range (BITS):
    bit_direction = input(f"Pin {i} Direction is: ")
    if bit_direction.lower() == 'out':
        DDR_value += pow(2,i)

DDR = format(DDR_value,'b')

file_h.write(f"void Init_{PORT}_DIR(void);")
file_c.write(f'#include "gpio_init.h"\n\nvoid Init_{PORT}_DIR(void)\n'+'{\n\t'+'DDR'+PORT[-1]+'= 0b'+format(DDR_value,'b')+'\n'+'}\n')



