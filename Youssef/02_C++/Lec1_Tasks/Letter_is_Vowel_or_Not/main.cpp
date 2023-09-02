/***
   Autor      :     Youssef Adel Youssef
Description   :     Write Program to decide the letter is vowel or not
***/

#include <iostream>

int main() 
{
    char letter;

    // Input a letter
    std::cout << "Enter a letter: ";
    std::cin >> letter;

    // Convert the letter to uppercase for case-insensitive comparison
    letter = std::toupper(letter);

    // Check if the letter is a vowel
    bool is_vowel = (letter == 'A' || letter == 'E' || letter == 'I' || letter == 'O' || letter == 'U');

    if (is_vowel) {
        std::cout << letter << " is a vowel." << std::endl;
    } else {
        std::cout << letter << " is not a vowel." << std::endl;
    }

    return 0;
}
