/***
   Autor      :     Youssef Adel Youssef
Description   :     Write program to test function overloading
***/

#include <iostream> // Include the input-output stream library.

// Define a function 'Multiply' that takes two integers and returns their product.
int Multiply(int x, int y)
{
    return x * y;
}

// Define another version of the 'Multiply' function that takes two doubles and returns their product.
double Multiply(double x, double y)
{
    return x * y;
}

int main() 
{
    int Result1 = Multiply(2, 5);               // Call the 'Multiply' function with integers and store the result in 'Result1'.
    double Result2 = Multiply(2.5, 5.5);        // Call the 'Multiply' function with doubles and store the result in 'Result2'.

    // Output the results along with labels.
    std::cout << "Result1: " << Result1 << std::endl;
    std::cout << "Result2: " << Result2 << std::endl;
}
