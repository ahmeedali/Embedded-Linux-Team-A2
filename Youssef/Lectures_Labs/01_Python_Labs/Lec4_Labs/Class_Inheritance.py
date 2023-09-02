""" 
   Autor      :   Youssef Adel Youssef
Description   :   write a Python program for Class to describe Class Inheritance
"""

class animal:
    name = ""
    
    def __init__(self) -> None:
        print("Constructor is Called")
        
    def eat(self):
        print("eat food")

    def __del__(self):
        print("Destructor is Called")
        
        
class cat(animal):
    
    def __init__(self):
        print("Constructor is Called")
        
    def sound(self):
        print("Meaouuu")

    def __del__(self):
        print("Destructor is Called")
        
mycat = cat()
mycat.eat()
mycat.sound()