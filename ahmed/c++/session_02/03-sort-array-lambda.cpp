#include <algorithm>
#include <array>
#include <iostream>

int main() {

  std::array<int, 10> arr{{5, 8, 9, 3, 4, 1, 2, 34, 21, 45}};

  std::sort (arr.begin(), arr.end(), [](int a, int b) { return a < b ;});


  for (int i : arr)
  {  std::cout<<i <<" ";  }

    std::cout <<"\n";
   std::sort (arr.begin(), arr.end(), [](int a, int b) { return a > b ;});


  for (int i : arr)
  {  std::cout<<i <<" ";  }
  std::cout <<"\n";
}
