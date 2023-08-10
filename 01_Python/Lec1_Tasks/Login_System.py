""" 
   Autor      :     Youssef Adel Youssef
Description   :     Handle the login system by Name and password.
"""

Login_Keys = {
"ahmed" : 1394,
"ali" : 6078,
"amr" : 9345    
}

Name = input("Please Enter Your Name :")
Key = int(input("Please Enter Your Password :"))

Parsing_Name = Name.strip().lower()

for i in range(0,3):
    
    if Login_Keys[Parsing_Name] == Key:
        print("Welcome {}".format(Parsing_Name))
        break
    
    else :
        print("Wrong Password")
        break