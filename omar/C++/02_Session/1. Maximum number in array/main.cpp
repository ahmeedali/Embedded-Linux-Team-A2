#include <array>
#include <iostream>
#include <algorithm>

int array[6] = {88,75,106,15,30,40};

int findMax(int arr[], int arr_size){
  int max = 0;
  
  max = *std::max_element(arr, arr+arr_size);

  return max;
}

int main(int argc, const char **argv) {

  int array_size = sizeof(array)/sizeof(array[0]);

  std::cout << findMax(array, array_size) << std::endl;
  
  return 0;
}