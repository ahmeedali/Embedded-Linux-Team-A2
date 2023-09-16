#include <algorithm>
#include <iostream>

int array[6] = {88,21,106,15,30,40};

void printArray(int arr[], const int arr_size);

void printArray(int arr[], const int arr_size){
  std::cout << "[";
  for(int i = 0; i < arr_size; i++){
    std::cout << arr[i];
    if(i < arr_size-1){
      std::cout << ", ";
    }
  }
  std::cout << "]" << std::endl;
}

int main(int argc, const char **argv) {

  int array_size = sizeof(array)/sizeof(array[0]);

  std::cout << "Original array" << std::endl;
  printArray(array, array_size);
  std::cout << "" << std::endl;
  
  // sorting ascendingly using lambda expression
  std::sort(array, array+array_size, [](int a, int b){return a < b;});
  
  std::cout << "Ascedingly sorted array" << std::endl;
  printArray(array, array_size);
  std::cout << "" << std::endl;

  // sorting descendingly using lambda expression
  std::sort(array, array+array_size, [](int a, int b){return a > b;});
  
  std::cout << "Descendingly sorted array" << std::endl;
  printArray(array, array_size);

  return 0;
}