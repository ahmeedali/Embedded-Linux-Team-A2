/***
   Autor      :     YOUSSEF ADEL YOUSSEF
Description   :     Calculate accumulate of array without using loops
***/

#include <iostream>
#include <numeric>      // Include the numeric header for std::accumulate

int main() 
{
    int arr[] = {1, 2, 3, 4, 5, 6, 7, 8, 9};
    
    // Calculate the size of the array
    int size = sizeof(arr) / sizeof(arr[0]);    

    // Calculate the sum of the array using std::accumulate
    int sum = std::accumulate(arr, arr + size, 0);

    std::cout << "Sum of the array elements: " << sum << std::endl;

    return 0;
}
