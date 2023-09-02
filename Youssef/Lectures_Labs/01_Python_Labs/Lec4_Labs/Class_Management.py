""" 
   Autor      :   Youssef Adel Youssef
Description   :   write a Python program for Class Management for constructor, Destructor and Documentation
"""

class Person:
    """
    This is a simple example class to demonstrate docstring formatting

    Attributes :
        name (str): This attribute store string value 
        age (int) : This attribute store int value
        
    Methods :
        Greeting() : This method performs some action and demostrates how to document method
        
    Example :
        >>> obj = Person()
        >>> obj.Greeting()
        Action Complete
    """
    name = ""
    age = 0
    
    def __init__(self, name, age) -> None:
        """
        Constructor for the Person Class
        
        Initialize the name and age attributes
        """
        print("Constructor is Called")
        self.name = name
        self.age = age
        
    
    def __str__(self):
        return ("Description of the class")
    
    
    def Greeting(self):
        """
        Performe an action and print the message
        
        This method print informations and demostrates how the document methods with description
        """
        print(f"Name : {self.name}")
        print(f"Age  : {self.age}")
        
        
    def __del__(self):
        """
        Destructor for the Person Class
        
        Initialize the name and age attributes
        """
        
        print("Destructor is Called")
        
                
Youssef = Person("Youssef",27)
print(Youssef)
print(Youssef.__doc__)
print(Youssef.Greeting.__doc__)
Youssef.Greeting()


Ahmed = Person("Ahmed" , 31)
Ahmed.Greeting()