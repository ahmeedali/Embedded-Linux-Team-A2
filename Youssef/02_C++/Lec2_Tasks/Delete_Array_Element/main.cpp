/***
   Autor      :     Youssef Adel Youssef
Description   :     Write program to delete number in array
***/

#include <iostream>
#include <algorithm>        // for std::remove

int main() {
    int arr[30];            // Maximum size of the array
    int size;               // Logical size of the array (number of elements)

    // Ask the user for the number of elements in the array
    std::cout << "Enter the number of elements in the array where maximum number is 30 : ";
    std::cin >> size;

    // Ask the user to enter the elements of the array
    std::cout << "Enter " << size << " integers separated by spaces: ";
    for (int i = 0; i < size; i++) {
        std::cin >> arr[i];
    }

    // Ask the user for the number to delete
    int target;
    std::cout << "Enter the number to delete: ";
    std::cin >> target;

    // Use std::remove to "delete" the target number
    int* newEnd = std::remove(arr, arr + size, target);

    // Calculate the new logical size of the array
    size = newEnd - arr;

    // Print the modified array
    std::cout << "Modified Array: ";
    for (int i = 0; i < size; i++) {
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;

    return 0;
}
