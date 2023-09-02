/***
   Autor      :     Youssef Adel Youssef
Description   :     Write Program to change from decimal to binary and vice versa
***/

#include <iostream>
#include <bitset>
#include <string>

int main() 
{
    int choice;
    std::cout << "Choose an option:\n";
    std::cout << "1. Decimal to Binary\n";
    std::cout << "2. Binary to Decimal\n";
    std::cin >> choice;

    if (choice == 1) 
    {
        int decimal;
        std::cout << "Enter a decimal number: ";
        std::cin >> decimal;

        // Convert decimal to binary
        std::bitset<32> binary(decimal); // Assuming 32-bit representation
        std::cout << "Binary representation: " << binary << std::endl;
    } 
    
    else if (choice == 2) {
        std::string binary_str;
        int decimal = 0;

        std::cout << "Enter a binary number: ";
        std::cin >> binary_str;

        // Convert binary to decimal
        for (char digit : binary_str) {
            decimal = (decimal << 1) + (digit - '0');
        }

        std::cout << "Decimal representation: " << decimal << std::endl;
    } 
    
    else 
    {
        std::cout << "Invalid choice!" << std::endl;
    }

    return 0;
}
