#include <array>
#include <iostream>
#include <algorithm>
#include <iterator>

int array[6] = {88,75,106,15,30,40};

int search(const int arr[], const int arr_size, const int element){
  int index = 0;
  const int* iterator = std::find(arr, arr+arr_size, element);
  
  if(iterator != (arr+arr_size)){
    index = static_cast<int>((iterator-arr)-1);
    std::cout << "Element found at: " << (iterator-arr)-1 << std::endl;
  }
  else{
    index = arr_size;
    std::cout << "Element not found" << std::endl;
  }

  return index;
}

int main(int argc, const char **argv) {

  int array_size = sizeof(array)/sizeof(array[0]);

  search(array, array_size, 5);
  search(array, array_size, 30);

  return 0;
}