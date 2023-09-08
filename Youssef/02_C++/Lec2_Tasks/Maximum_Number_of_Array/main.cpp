/***
   Autor      :     Youssef Adel Youssef
Description   :     Create a function to ﬁnd the maximum number of array
***/

#include <algorithm>  // Include the necessary library for the std::max_element function
#include <iostream>

// Function to find the maximum element in an array
int max_Element(int arr[], int size) 
{
    // Find the maximum element in the 'arr' array using std::max_element
    int* Max_Elemnt = std::max_element(arr, arr + size);

    if (Max_Elemnt != arr + size) {
        // If the maximum element is found, return its value
        return *Max_Elemnt;
    } else {
        // If the array is empty, print a message and return -1
        std::cout << "Array is empty." << std::endl;
        return -1;
    }
}

int main() 
{
    int arr[] = {15, 20, 80, 10, 5, 6, 7};
    int arr_size = sizeof(arr) / sizeof(arr[0]);
    
    // Call the 'max_Element' function to find the maximum element in the 'arr' array
    int Result = max_Element(arr, arr_size);
    
    // Check if a valid result was obtained and print it
    if (Result != -1)
        std::cout << "The Maximum Number = " << Result << std::endl;

    return 0;
}
