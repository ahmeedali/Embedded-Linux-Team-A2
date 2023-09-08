/***
   Autor      :     Youssef Adel Youssef
Description   :     Write program to test lambda expression
***/

#include <iostream>

int main() 
{
    // Define a lambda function 'fun' that takes two integers and returns their sum.
    auto fun = [](int x, int y) 
    {
        return x + y;
    };
    
    // Call the 'fun' lambda function with arguments 2 and 4 and output the result.
    std::cout << fun(2, 4) << std::endl;

    // Define and immediately invoke an anonymous lambda function that takes two integers.
    // This lambda function prints the values of 'x' and 'y'.
    [](int x, int y) {
        std::cout << "X = " << x << std::endl;
        std::cout << "Y = " << y << std::endl;
    }(2, 4);

    return 0;
}
