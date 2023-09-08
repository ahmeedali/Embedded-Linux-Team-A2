/***
   Autor      :     Youssef Adel Youssef
Description   :     Write program to test function default parameters
***/

#include <iostream>
#include <string>

void printMessage(std::string message = "Hello , World")
{
    std::cout << message << std::endl;
}

int main()
{
    printMessage();
    printMessage("Hi");
}