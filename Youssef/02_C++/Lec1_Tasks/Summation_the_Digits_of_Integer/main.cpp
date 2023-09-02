/***
   Autor      :     Youssef Adel Youssef
Description   :     Write Program to summation the digits of integer entered by user
***/

#include <iostream>

int main() {
    int num, sum = 0;

    // Input an integer from the user
    std::cout << "Enter an integer: ";
    std::cin >> num;

    // Calculate the summation of digits
    int temp = num;
    while (temp != 0) {
        int digit = temp % 10;
        sum += digit;
        temp /= 10;
    }

    // Display the result
    std::cout << "The summation of digits of " << num << " is : " << sum << std::endl;

    return 0;
}
