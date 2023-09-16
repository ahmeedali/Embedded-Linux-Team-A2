#include <iomanip>
#include <iostream>

bool is_right_triangle(int a, int b, int c) {

  return (((a * a) + (b * b) == (c * c)) || ((a * a) + (c * c) == (b * b)) ||
          ((b * b) + (c * c) == (a * a)));
}

int main(int argc, const char **argv) {

  if (is_right_triangle(12,16,20)) {
    std::cout << "This is a right angled triangle" << std::endl;
  } else {
    std::cout << "This is not a right angled triangle" << std::endl;
  }
  return 0;
}