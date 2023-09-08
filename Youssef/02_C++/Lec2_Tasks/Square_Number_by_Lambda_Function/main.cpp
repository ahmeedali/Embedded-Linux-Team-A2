/***
   Autor      :     Youssef Adel Youssef
Description   :     Write a lambda function to calculate the square of a given number.
***/

#include <iostream>

int main()
{
    // Define a lambda function to calculate the square
    auto square = [](int x) { return x * x; };

    // Input a number
    int number;
    std::cout << "Enter a number: ";
    std::cin >> number;

    // Calculate and display the square using the lambda
    int result = square(number);
    std::cout << "Square of " << number << " is: " << result << std::endl;

    return 0;
}
