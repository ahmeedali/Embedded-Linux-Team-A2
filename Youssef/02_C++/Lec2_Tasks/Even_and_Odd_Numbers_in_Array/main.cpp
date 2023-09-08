/***
   Autor      :     Youssef Adel Youssef
Description   :     Write program to ﬁnd the even and odd numbers in the array
***/

#include <iostream>

int main() {
    // Create an array of integers
    int numbers[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

    // Calculate the size of the array
    int size = sizeof(numbers) / sizeof(numbers[0]);

    // Create arrays to store even and odd numbers
    int evenNumbers[size];
    int oddNumbers[size];

    // Initialize counts for even and odd numbers
    int evenCount = 0;
    int oddCount = 0;

    // Iterate through the array
    for (int i = 0; i < size; i++) 
    {
        if (numbers[i] % 2 == 0) 
        {
            evenNumbers[evenCount++] = numbers[i]; // Add even number to evenNumbers array
        } 
        
        else {
            oddNumbers[oddCount++] = numbers[i]; // Add odd number to oddNumbers array
        }
    }

    // Print even numbers
    std::cout << "Even numbers: ";
    for (int i = 0; i < evenCount; i++) 
    {
        std::cout << evenNumbers[i] << " ";
    }
    std::cout << std::endl;

    // Print odd numbers
    std::cout << "Odd numbers: ";
    for (int i = 0; i < oddCount; i++) 
    {
        std::cout << oddNumbers[i] << " ";
    }
    std::cout << std::endl;

    return 0;
}
