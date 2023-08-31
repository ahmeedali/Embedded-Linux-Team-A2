#include <iostream>
#include<vector>



bool IsVowel(std :: string character);

int main()
{
  std :: string character;
  std :: cout << "Enter a character: ";
  std :: cin >> character;
  if (IsVowel(character))
  std::cout << "The character " << character <<" is vowel"<< std::endl;
  else 
   std::cout << "The character " << character <<" is consonant" << std::endl;

return 0; 
}

bool IsVowel(std :: string character){
std:: vector<std::string> vowels = { "a", "e", "i", "o", "u","A", "E", "I", "O", "U"};
 for (int i= 0; i<=vowels.size(); i++){
 if (vowels[i] == character)
    return true;
 }
 return false;
}