/***
   Autor      :     YOUSSEF ADEL YOUSSEF
Description   :     Check if all the array is even
***/

#include <iostream>
#include <algorithm>

int main() 
{
    int arr[] = {2, 4, 6, 8, 10}; 

    // Calculate the size of the array
    int size = sizeof(arr) / sizeof(arr[0]); 

    // Lambda function checks if the element is even
    bool allEven = std::all_of(arr, arr + size, [](int element) {   
        return element % 2 == 0; 
    });

    if (allEven) 
    {
        std::cout << "All elements in the array are even." << std::endl;
    } 
    
    else 
    {
        std::cout << "Not all elements in the array are even." << std::endl;
    }

    return 0;
}

