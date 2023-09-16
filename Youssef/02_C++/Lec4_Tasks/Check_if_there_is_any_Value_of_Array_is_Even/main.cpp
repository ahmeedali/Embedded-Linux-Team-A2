/***
   Autor      :     YOUSSEF ADEL YOUSSEF
Description   :     Check if there is any value of array is even
***/

#include <iostream>
#include <algorithm>

int main() {
    int arr[] = {1, 3, 5, 8, 7, 9}; // Example array
    int size = sizeof(arr) / sizeof(arr[0]);

    // Lambda function checks if the element is even
    bool hasEven = std::any_of(arr, arr + size, [](int element) {
        return element % 2 == 0;
    });

    if (hasEven) 
    {
        std::cout << "The array contains at least one even value." << std::endl;
    } 
    
    else 
    {
        std::cout << "The array does not contain any even values." << std::endl;
    }

    return 0;
}
