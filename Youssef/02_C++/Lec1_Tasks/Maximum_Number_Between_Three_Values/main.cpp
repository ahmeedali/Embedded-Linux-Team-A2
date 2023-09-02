/***
   Autor      :     Youssef Adel Youssef
Description   :     Write Program to find maximum number between three values
***/

#include <iostream>

int main() 
{
    int num1, num2, num3;

    // Input three numbers
    std::cout << "Enter three numbers: ";
    std::cin >> num1 >> num2 >> num3;

    // Find the maximum among the three numbers
    int max_num;

    if (num1 >= num2 && num1 >= num3) 
    {
        max_num = num1;
    } 
    
    else if (num2 >= num1 && num2 >= num3) 
    {
        max_num = num2;
    } 
    
    else 
    {
        max_num = num3;
    }

    // Another solution to Find the maximum among the three numbers by using inline conditional
    // max_num = (num1 >= num2 && num1 >= num3) ? num1 : ((num2 >= num1 && num2 >= num3) ? num2 : num3);


    // Display the maximum number
    std::cout << "The maximum number is : " << max_num << std::endl;

    return 0;
}