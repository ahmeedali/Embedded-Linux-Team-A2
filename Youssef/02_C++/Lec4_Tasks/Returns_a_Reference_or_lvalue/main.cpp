/***
   Autor      :     YOUSSEF ADEL YOUSSEF
Description   :     Returns a Reference or lvalue
***/

#include <iostream>

int x = 0;

int& f() {
    return x;
}

int main() {
    f() = 10;   // Assign 10 to the object referred to by the reference returned by f()
    std::cout << x << std::endl; // Outputs: 10

    f() = 0;    // Assign 0 to the same object
    std::cout << x << std::endl; // Outputs: 0

    return 0;
}
