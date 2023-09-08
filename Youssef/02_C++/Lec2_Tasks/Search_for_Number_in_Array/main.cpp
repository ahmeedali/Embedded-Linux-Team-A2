/***
   Autor      :     Youssef Adel Youssef
Description   :     create a function to search to the number in the array which number is taken from user
***/

#include <iostream>

// Function to check if a target value exists in the array
bool max_Element(int arr[], int size, int target) 
{
    for (int iter = 0; iter < size; iter++) 
    {
        if (arr[iter] == target) 
        {
            return true;  // Number found
        }
    }
    return false;  // Number not found
}

int main() {
    int arr[] = { 15, 20, 80, 10, 5, 6, 7 };
    int TargetValue = 0;
    int size = sizeof(arr) / sizeof(arr[0]);

    // Input the target value
    std::cout << "Enter an integer: ";
    std::cin >> TargetValue;

    // Check if the target value is found in the array
    bool Result = max_Element(arr, size, TargetValue);

    if (Result == true)
        std::cout << "The Number is found." << std::endl;
    else
    {
        std::cout << "The Number is not found." << std::endl;        
    }
    return 0;
}
