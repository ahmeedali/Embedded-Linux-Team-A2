/***
   Autor      :     Youssef Adel Youssef
Description   :     Use lambda functions to sort an array of integers in ascending and descending order.
***/

#include <iostream>
#include <algorithm>

int main() 
{
    // Create an array of integers
    int numbers[] = {5, 2, 9, 1, 5, 6, 3, 8};
    int size = sizeof(numbers) / sizeof(numbers[0]);

    // Sort in ascending order using a lambda
    std::sort(numbers, numbers + size, [](int a, int b) { return a < b; });

    std::cout << "Ascending Order: ";
    for (int i = 0; i < size; ++i) 
    {
        std::cout << numbers[i] << " ";
    }
    std::cout << std::endl;

    // Sort in descending order using a lambda
    std::sort(numbers, numbers + size, [](int a, int b) { return a > b; });

    std::cout << "Descending Order: ";
    for (int i = 0; i < size; ++i) 
    {
        std::cout << numbers[i] << " ";
    }
    std::cout << std::endl;

    return 0;
}
