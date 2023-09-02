""" 
   Autor      :   Youssef Adel Youssef
Description   :   Write a Python program for Threading 
"""

import threading

def Task1(num):
    for i in range(0,num):
        print("Task1")


def Task2(num):
    for i in range(0,num):
        print("Task2")

# Create Thread
t1 = threading.Thread(target=Task1 , args=(5,))
t2 = threading.Thread(target=Task2 , args=(5,))

# Start Thread 1
t1.start()

# Start Thread 2
t2.start()

# Wait until Task1 is completely executed
t1.join()

# Wait until Task2 is completely executed
t2.join()

# Both thread completely executed
print("Done")

