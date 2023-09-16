/***
   Autor      :     YOUSSEF ADEL YOUSSEF
Description   :     Check if the character is digit
***/

#include <iostream>
#include <cctype>       // Include the cctype header, which provides functions for character-based operations

int main() 
{
    char character;

    std::cout << "Enter a character: ";
    std::cin >> character;

    if (std::isdigit(character)) 
    {
        std::cout << "The input is a digit." << std::endl;
    } 
    
    else 
    {
        std::cout << "The input is not a digit." << std::endl;
    }

    return 0;
}
