#include <iostream>

auto square = [](int n) -> int{ return n*n;};

int main(int argc, const char **argv) {

  std::cout << square(5) << std::endl;
  std::cout << square(9) << std::endl;

  return 0;
}