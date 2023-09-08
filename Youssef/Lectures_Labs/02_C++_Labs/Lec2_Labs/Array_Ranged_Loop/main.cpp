/***
   Autor      :     Youssef Adel Youssef
Description   :     Write program to test array ranged loop
***/

#include <iostream>                                     // Include the input-output stream library.

int main()  
{
    int Arr[] = {10, 15, 12, 20, 30, 14};               // Declare an integer array named 'Arr' and initialize it with values.

    for (int value : Arr)                               // Start a for-each loop to iterate through the elements of the 'Arr' array.
    {
        std::cout << value << "   ";                    // Output the current element of the array followed by three spaces.
    }
    std::cout << std::endl; 
}
