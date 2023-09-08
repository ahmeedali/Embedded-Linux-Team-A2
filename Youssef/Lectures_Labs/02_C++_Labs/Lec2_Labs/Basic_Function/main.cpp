/***
   Autor      :     Youssef Adel Youssef
Description   :     Write program to test basic function
***/

#include <iostream>

int add(int x , int y)
{
    return x+y;
}

int main()
{
    int Result = add(2, 3);
    std::cout<< "Sum = " << Result << std::endl;
}