/***
   Autor      :     Youssef Adel Youssef
Description   :     Merge two arrays together
***/

#include <iostream>
#include <algorithm>

int main() {
    int arr1[] = {1, 2, 3, 4};
    int size1 = sizeof(arr1) / sizeof(arr1[0]);

    int arr2[] = {5, 6, 7};
    int size2 = sizeof(arr2) / sizeof(arr2[0]);

    int mergedSize = size1 + size2;
    int mergedArray[mergedSize];  // Create an array to store the merged elements

    // Using std::merge to merge arr1 and arr2
    std::merge(arr1, arr1 + size1, arr2, arr2 + size2, mergedArray);

    // Print the merged array
    std::cout << "Merged Array: ";
    for (int i = 0; i < mergedSize; i++) 
    {
        std::cout << mergedArray[i] << " ";
    }
    std::cout << std::endl;

    return 0;
}

