/***
   Autor      :     Youssef Adel Youssef
Description   :     Write Program to Create a table for AscII code
***/
 
#include <iostream>     // Include the standard input/output stream library for input/output operations.

int main() {
    std::cout << "ASCII Table" << std::endl;
    std::cout << "-----------" << std::endl;
    std::cout << "ASCII Character  |  Decimal" << std::endl;
    std::cout << "------------------------" << std::endl;

    for (int i = 0; i < 128; i++) 
    {
        std::cout <<"|     " << char(i) << "     |     " << i << "     |"<< std::endl;
    }

    return 0;
}
