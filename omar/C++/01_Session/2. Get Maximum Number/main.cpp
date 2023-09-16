#include <algorithm>
#include <iomanip>
#include <iostream>

bool comp(int a, int b) { return a < b; }

int get_max_number(int n1, int n2) {

  return std::max(n1, n2, comp);
}

int get_max_number(int n1, int n2, int n3) {

  return std::max({n1, n2, n3}, comp);
}

int main(int argc, const char **argv) {

  int max = get_max_number(1,7);
  std::cout << max << std::endl;
  return 0;
}