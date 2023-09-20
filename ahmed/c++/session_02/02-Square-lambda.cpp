#include <iostream>

int main() {
    int num;
    std::cout << "Enter a number: ";
    std::cin >> num;
    std::cout << "Square of " << num << " is " << [](int x) { return x * x; }(num) << std::endl;

    return 0;
}