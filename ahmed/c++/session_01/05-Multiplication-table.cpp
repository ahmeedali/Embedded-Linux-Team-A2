#include <iostream>

int main ()
{
    int number , result; 
    std::cout << "Enter a number: ";
    std::cin >> number;
     for (int i = 0; i <= 10 ; i++)
      std :: cout << i << "  *  " << number<< " = " << i*number << std::endl;


    return 0; 
}