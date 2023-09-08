/***
   Autor      :     Youssef Adel Youssef
Description   :     Write Program to test array with function
***/

#include <iostream>                                         // Include the input-output stream library.


void printArray(int arr[], int size)                        // Define a function named 'printArray' that takes an integer array and its size as parameters.
{
    for (int i = 0; i < size; i++)                          // Start a for loop to iterate through the elements of the array.
    {
        std::cout << arr[i] << "  ";                        // Output the current element of the array followed by two spaces.
    }
    std::cout << std::endl;                                 // Output an end-of-line character to move to the next line.
}

int main() 
{
    int Array[] = {10, 15, 12, 20, 30, 14};                 // Declare an integer array named 'Array' and initialize it with values.
    int Array_size = sizeof(Array) / sizeof(Array[0]);      // Calculate the size of the array by dividing the total size by the size of one element.
    printArray(Array, Array_size);                          // Call the 'printArray' function to print the elements of the array.
    return 0; 
}
