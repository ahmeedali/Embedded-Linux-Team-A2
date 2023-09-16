#include <array>
#include <iostream>
#include <algorithm>

int array[6] = {88,15,106,15,30,40};

int deleteElement(int arr[], const int arr_size, const int element){
  int new_size = arr_size;
  int found = 0;
  
  for(int i = 0; i < arr_size; i++){
    if(arr[i] == element){
      found++;
      new_size--;
      continue;
    }
    if(found){
      arr[i-found]=arr[i];
    }
  }

  if(!found){
    std::cout << "Element " << element << " not found" << std::endl;
  }
  else{
    std::cout << "Element " << element << " deleted" << std::endl;
  }

  return new_size;
}

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
  
  array_size = deleteElement(array, array_size, 15);
  
  std::cout << "New array" << std::endl;
  printArray(array, array_size);
  
  array_size = deleteElement(array, array_size, 40);
  
  std::cout << "New array" << std::endl;
  printArray(array, array_size);

  array_size = deleteElement(array, array_size, 200);

  return 0;
}