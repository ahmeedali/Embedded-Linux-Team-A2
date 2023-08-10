""" 
   Autor      :     Youssef Adel Youssef
Description   :     Test whether a letter passed is a vowel or not.
"""

def Is_Vowel(Char):
    All_Vowels = "aeiou"
    return Char in All_Vowels

Ch = (input("Enter the Character for Test : ")).lower()
print(Is_Vowel(Ch))

