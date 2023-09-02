/***
   Autor      :     Youssef Adel Youssef
Description   :     Write Program to Create a multiplication table
***/

#include <iostream>

int main() 
{
    int tableSize;

    // Input the size of the multiplication table
    std::cout << "Enter the size of the multiplication table: ";
    std::cin >> tableSize;

    // Generate and print the multiplication table
    for (int i = 1; i <= tableSize; i++) 
    {
        for (int j = 1; j <= 12; j++) 
        {
            std::cout << i << " x " << j << " = " << i * j << std::endl;
        }

        std::cout << std::endl;
        std::cout << "-------------------" << std::endl;
        std::cout << std::endl;
    }

    return 0;
}
