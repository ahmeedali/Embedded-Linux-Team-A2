#Lab(04) Classes :
class person :
    name="person"

    def __init__(self,name) :
      self.name=name
      print(self.name)
      print("constructor p")
      

    def  walk(self):
      print("walking...")
      print(self)       

    def __del__(self):
       print("destructor p")  

class Male(person) :
   
   def __init__(self, name):
      super().__init__(name)         #super enables us to call the constructor of the parent class
      print(self.name)               # self access the instance itself
      print(super().name)            #super acsses the blue print of the class not that of the instance
      print("constructor M")


   def  run(self):
      print("Runing...") 
      print(super().address()) 

   def  __del__(self):
      super().__del__() 
      print("destructor M") 
   


player1=Male("BRRR")
player1.run()
player1.walk()
print(player1.name)
###########################################################################################################
