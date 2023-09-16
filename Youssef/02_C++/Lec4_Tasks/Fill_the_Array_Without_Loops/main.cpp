/***
   Autor      :     YOUSSEF ADEL YOUSSEF
Description   :     Fill array from 10 to 10000 sequentially without loops
***/

#include <iostream>
#include <numeric>  // Include the numeric header for std::iota

int main() 
{
    const int size = 9991;  // Size of the array (10000 - 10 + 1)
    int arr[size];          // Declare an array

    // Use std::iota to fill the array with sequential values from 10 to 10000
    std::iota(arr, arr + size, 10);

    // Print the first 100 elements to verify
    for (int i = 0; i < 100; ++i) 
    {
        std::cout << arr[i] << " ";
    }

    return 0;
}
