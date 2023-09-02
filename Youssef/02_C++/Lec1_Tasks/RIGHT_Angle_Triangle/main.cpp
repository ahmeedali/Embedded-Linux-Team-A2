/***
   Autor      :     Youssef Adel Youssef
Description   :     Write Program to decide the values represent RIGHT angle triangle or not
***/

#include <iostream>

int main() {
    double a, b, c;

    // Input the lengths of the three sides
    std::cout << "Enter the length of side a: ";
    std::cin >> a;
    std::cout << "Enter the length of side b: ";
    std::cin >> b;
    std::cout << "Enter the length of side c: ";
    std::cin >> c;


    // Check if it forms a right-angle triangle
    bool is_right_triangle = ( a*a + b*b == c*c ) || ( a*a + c*c == b*b ) || ( b*b + c*c == a*a );

    if (is_right_triangle) {
        std::cout << "It represents a right-angle triangle." << std::endl;
    } else {
        std::cout << "It does not represent a right-angle triangle." << std::endl;
    }

    return 0;
}
